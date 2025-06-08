import streamlit as st
import joblib
import pandas as pd
import numpy as np
import warnings
from lightgbm import LGBMClassifier
import os

warnings.filterwarnings("ignore")

st.set_page_config(
    page_title="Student Academic Success Predictor",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown("""
<style>
    .main { padding: 2rem; }
    .stButton > button {
        width: 100%;
        background-color: #4CAF50;
        color: white;
        font-weight: bold;
        padding: 10px;
        border-radius: 5px;
    }
    .stButton > button:hover { background-color: #45a049; }
    .result-box {
        padding: 20px;
        border-radius: 10px;
        margin-top: 20px;
        text-align: center;
    }
    .success { background-color: rgba(76, 175, 80, 0.1); border: 1px solid #4CAF50; }
    .dropout { background-color: rgba(244, 67, 54, 0.1); border: 1px solid #F44336; }
    .enrolled { background-color: rgba(33, 150, 243, 0.1); border: 1px solid #2196F3; }
    h1, h2 { text-align: center; }
    .stExpander { border-radius: 8px; margin-bottom: 10px; }
</style>
""", unsafe_allow_html=True)

@st.cache_resource
def load_model():
    model_path = os.path.join(os.path.dirname(__file__), 'model_lgb.pkl')
    return joblib.load(model_path)

def predict(data, model):
    if isinstance(data, pd.DataFrame):
        X = data
    elif isinstance(data, (list, pd.Series, np.ndarray)):
        X = pd.DataFrame(data, columns=model.feature_names_in_)
    else:
        raise ValueError("Input data must be a DataFrame, list, Series, or numpy array")
    y_pred = model.predict(X)
    return y_pred[0]

st.title("🎓 Student Academic Success Predictor")
st.markdown("")
st.markdown("")
st.markdown("")
st.markdown("### Predict student dropout and academic success based on various factors.")

try:
    with st.spinner("Loading model..."):
        model = load_model()
    st.success("Model loaded successfully!")
except Exception as e:
    st.error(f"Error loading model: {str(e)}")
    st.stop()

st.sidebar.title("Input Features")
st.sidebar.markdown("Please fill in the following features to predict student outcome")

with st.sidebar:
    with st.expander("Personal Information", expanded=True):
        gender = st.selectbox("Gender", options=[(1, "Male"), (0, "Female")], format_func=lambda x: x[1])
        age = st.number_input("Age at Enrollment", min_value=16, max_value=70, value=20)
        marital_status = st.selectbox(
            "Marital Status",
            options=[
                (1, "Single"), (2, "Married"), (3, "Widower"),
                (4, "Divorced"), (5, "Facto union"), (6, "Legally separated")
            ],
            format_func=lambda x: x[1]
        )
        international = st.selectbox("International Student", options=[(1, "Yes"), (0, "No")], format_func=lambda x: x[1])
        displaced = st.selectbox("Displaced Person", options=[(1, "Yes"), (0, "No")], format_func=lambda x: x[1])
        nacionality = st.number_input("Nationality Code", min_value=1, max_value=100, value=1)
        special_needs = st.selectbox("Educational Special Needs", options=[(1, "Yes"), (0, "No")], format_func=lambda x: x[1])
    with st.expander("Family Background"):
        mothers_qualification = st.number_input("Mother's Qualification", min_value=1, max_value=34, value=1)
        fathers_qualification = st.number_input("Father's Qualification", min_value=1, max_value=34, value=1)
        mothers_occupation = st.number_input("Mother's Occupation", min_value=1, max_value=46, value=1)
        fathers_occupation = st.number_input("Father's Occupation", min_value=1, max_value=46, value=1)
    with st.expander("Application Details"):
        app_mode = st.number_input("Application Mode", min_value=1, max_value=17, value=1)
        app_order = st.number_input("Application Order", min_value=0, max_value=9, value=1)
        course = st.number_input("Course Code", min_value=1, max_value=17, value=1)
        daytime_evening = st.selectbox("Attendance Type", options=[(1, "Daytime"), (0, "Evening")], format_func=lambda x: x[1])
        previous_qualification = st.number_input("Previous Qualification", min_value=1, max_value=17, value=1)
        prev_qualification_grade = st.number_input("Previous Qualification Grade (0-200)", min_value=0.0, max_value=200.0, value=120.0, step=0.1)
        admission_grade = st.number_input("Admission Grade (0-200)", min_value=0.0, max_value=200.0, value=120.0, step=0.1)
    with st.expander("Financial Status"):
        scholarship = st.selectbox("Scholarship Holder", options=[(1, "Yes"), (0, "No")], format_func=lambda x: x[1])
        debtor = st.selectbox("Debtor (Outstanding Tuition)", options=[(1, "Yes"), (0, "No")], format_func=lambda x: x[1])
        tuition_up_to_date = st.selectbox("Tuition Fees Up to Date", options=[(1, "Yes"), (0, "No")], format_func=lambda x: x[1])
    with st.expander("1st Semester Performance"):
        units_1st_credited = st.number_input("1st Sem Units Credited", min_value=0, max_value=20, value=0)
        units_1st_enrolled = st.number_input("1st Sem Units Enrolled", min_value=0, max_value=20, value=6)
        units_1st_evaluations = st.number_input("1st Sem Units Evaluations", min_value=0, max_value=20, value=6)
        units_1st_approved = st.number_input("1st Sem Units Approved", min_value=0, max_value=20, value=5)
        units_1st_grade = st.number_input("1st Sem Grade (0-20)", min_value=0.0, max_value=20.0, value=12.0, step=0.1)
        units_1st_without_evaluations = st.number_input("1st Sem Units Without Evaluations", min_value=0, max_value=20, value=0)
    with st.expander("2nd Semester Performance"):
        units_2nd_credited = st.number_input("2nd Sem Units Credited", min_value=0, max_value=20, value=0)
        units_2nd_enrolled = st.number_input("2nd Sem Units Enrolled", min_value=0, max_value=20, value=6)
        units_2nd_evaluations = st.number_input("2nd Sem Units Evaluations", min_value=0, max_value=20, value=6)
        units_2nd_approved = st.number_input("2nd Sem Units Approved", min_value=0, max_value=20, value=5)
        units_2nd_grade = st.number_input("2nd Sem Grade (0-20)", min_value=0.0, max_value=20.0, value=12.0, step=0.1)
        units_2nd_without_evaluations = st.number_input("2nd Sem Units Without Evaluations", min_value=0, max_value=20, value=0)
    with st.expander("Economic Indicators"):
        unemployment_rate = st.number_input("Unemployment Rate (%)", min_value=0.0, max_value=100.0, value=7.6, step=0.1)
        inflation_rate = st.number_input("Inflation Rate (%)", min_value=0.0, max_value=100.0, value=1.5, step=0.1)
        gdp = st.number_input("GDP ($)", min_value=0.0, max_value=1000000.0, value=19000.0, step=100.0)
    predict_button = st.button("Predict Student Outcome")

if predict_button:
    data = pd.DataFrame({
        'Marital_status': [marital_status[0]],
        'Application_mode': [app_mode],
        'Application_order': [app_order],
        'Course': [course],
        'Daytime_evening_attendance': [daytime_evening[0]],
        'Previous_qualification': [previous_qualification],
        'Previous_qualification_grade': [prev_qualification_grade],
        'Nacionality': [nacionality],
        'Mothers_qualification': [mothers_qualification],
        'Fathers_qualification': [fathers_qualification],
        'Mothers_occupation': [mothers_occupation],
        'Fathers_occupation': [fathers_occupation],
        'Admission_grade': [admission_grade],
        'Displaced': [displaced[0]],
        'Educational_special_needs': [special_needs[0]],
        'Debtor': [debtor[0]],
        'Tuition_fees_up_to_date': [tuition_up_to_date[0]],
        'Gender': [gender[0]],
        'Scholarship_holder': [scholarship[0]],
        'Age_at_enrollment': [age],
        'International': [international[0]],
        'Curricular_units_1st_sem_credited': [units_1st_credited],
        'Curricular_units_1st_sem_enrolled': [units_1st_enrolled],
        'Curricular_units_1st_sem_evaluations': [units_1st_evaluations],
        'Curricular_units_1st_sem_approved': [units_1st_approved],
        'Curricular_units_1st_sem_grade': [units_1st_grade],
        'Curricular_units_1st_sem_without_evaluations': [units_1st_without_evaluations],
        'Curricular_units_2nd_sem_credited': [units_2nd_credited],
        'Curricular_units_2nd_sem_enrolled': [units_2nd_enrolled],
        'Curricular_units_2nd_sem_evaluations': [units_2nd_evaluations],
        'Curricular_units_2nd_sem_approved': [units_2nd_approved],
        'Curricular_units_2nd_sem_grade': [units_2nd_grade],
        'Curricular_units_2nd_sem_without_evaluations': [units_2nd_without_evaluations],
        'Unemployment_rate': [unemployment_rate],
        'Inflation_rate': [inflation_rate],
        'GDP': [gdp]
    })
    with st.spinner("Generating prediction..."):
        try:
            prediction = predict(data, model)
            st.subheader("Prediction Result")
            outcome_dict = {
                0: {"label": "Dropout", "description": "Student likely to drop out", "color": "dropout", "icon": "🚫"},
                1: {"label": "Enrolled", "description": "Student likely to remain enrolled", "color": "enrolled", "icon": "⏳"},
                2: {"label": "Graduate", "description": "Student likely to graduate successfully", "color": "success", "icon": "🎓"}
            }
            outcome = outcome_dict.get(prediction, {"label": "Unknown", "description": "Unable to determine outcome", "color": "", "icon": "❓"})
            st.markdown(f"""
            <div class="result-box {outcome['color']}">
                <h1>{outcome['icon']} {outcome['label']}</h1>
                <h3>{outcome['description']}</h3>
            </div>
            """, unsafe_allow_html=True)
            if prediction == 0:
                st.info("💡 Risk factors for dropout may include poor academic performance, financial difficulties, or personal circumstances.")
                st.markdown("### Recommendations:")
                st.markdown("""
                - Consider providing additional academic support
                - Review financial aid options
                - Schedule academic counseling session
                """)
            elif prediction == 1:
                st.info("💡 The student is likely to remain enrolled but may need support to progress to graduation.")
                st.markdown("### Recommendations:")
                st.markdown("""
                - Monitor academic progress closely
                - Provide career guidance
                - Encourage participation in student support services
                """)
            elif prediction == 2:
                st.success("💡 The student shows strong indicators for academic success and graduation.")
                st.markdown("### Recommendations:")
                st.markdown("""
                - Consider advanced learning opportunities
                - Provide information about graduate studies
                - Encourage mentorship roles for other students
                """)
        except Exception as e:
            st.error(f"Error making prediction: {str(e)}")

st.markdown("---")
st.markdown("A117XBM150 - Fadhilah Nurrahmayanti")
