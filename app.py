import os
import pickle
import streamlit as st
from streamlit_option_menu import option_menu
import joblib

working_dir = os.getcwd()

# Set page configuration
st.set_page_config(page_title="Health Assistant",
                   layout="wide",
                   page_icon="🧑‍⚕️")

scaler = joblib.load(os.path.join(working_dir, 'models/scaler.pkl'))
scaler2 = joblib.load(os.path.join(working_dir, 'models/scaler2.pkl'))

# getting the working directory of the main.py
working_dir = os.path.dirname(os.path.abspath(__file__))

# loading the saved models
# used support vector machine
diabetes_model = joblib.load(os.path.join(working_dir, 'models/classifier.pkl'))
# used logistic regression
heart_disease_model = joblib.load(os.path.join(working_dir, 'models/logistic_regression.pkl'))
# best model for Parkinson's (Random Forest)
parkinsons_model = joblib.load('models/parkinsons_model_rf.pkl')    

# sidebar for navigation
with st.sidebar:
    selected = option_menu('Multiple Disease Prediction System',

                           ['Diabetes Prediction',
                            'Heart Disease Prediction'],
                            # 'Parkinsons Prediction',
                           menu_icon='hospital-fill',
                           icons=['activity', 'heart', 'person'],
                           default_index=0)


#1
# Diabetes Prediction Page
if selected == 'Diabetes Prediction':

    # page title
    st.title('Diabetes Prediction using ML')

    # getting the input data from the user
    col1, col2, col3 = st.columns(3)

    with col1:
        Pregnancies = st.number_input(
    "Pregnancies (count)", 
    min_value=0, 
    max_value=17, 
    step=1, 
    format="%d", 
    help="Normal range: 0-20 pregnancies. Type or use buttons."
)

    with col2:
        Glucose = st.number_input(
    "Glucose Level (mg/dL)", 
    min_value=50, 
    max_value=300, 
    step=1, 
    format="%d", 
    help="Normal range: 70–140 mg/dL. Type or use buttons."
)

    with col3:
        BloodPressure = st.number_input(
    "Blood Pressure (mmHg)", 
    min_value=40, 
    max_value=200, 
    step=1, 
    format="%d", 
    help="Normal range: 90/60-120/80 mmHg. Type or use buttons."
)

    with col1:
        SkinThickness = st.number_input(
    "Skin Thickness (mm)", 
    min_value=5, 
    max_value=99, 
    step=1, 
    format="%d", 
    help="Normal range: 12-28 mm. Type or use buttons."
)

    with col2:
        Insulin = st.number_input(
    "Insulin (μU/mL)", 
    min_value=14, 
    max_value=846, 
    step=1, 
    format="%d", 
    help="Normal range: 16-166 μU/mL. Type or use buttons."
)

    with col3:
        BMI = st.number_input(
    "BMI (kg/m²)", 
    min_value=15.0, 
    max_value=68.0, 
    step=0.1, 
    format="%.1f", 
    help="Normal range: 18.5-24.9 kg/m². Type or use buttons."
)

    with col1:
        DiabetesPedigreeFunction = st.number_input(
    "Diabetes Pedigree Function", 
    min_value=0.078, 
    max_value=2.42, 
    step=0.001, 
    format="%.3f", 
    help="Normal range: 0.1-2.5 (higher indicates stronger family history). Type or use buttons."
)

    with col2:
        Age = st.number_input(
    "Age (years)", 
    min_value=21, 
    max_value=81, 
    step=1, 
    format="%d", 
    help="Adult age in years. Type or use buttons."
)


    # code for Prediction
    diab_diagnosis = ''

    # creating a button for Prediction
if st.button('Diabetes Test Result'):
        
            user_input = [Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin,
                      BMI, DiabetesPedigreeFunction, Age]

            user_input = [float(x) for x in user_input]

            # Apply scaling
            user_input_scaled = scaler.transform([user_input])

            diab_prediction = diabetes_model.predict(user_input_scaled)
    

            if diab_prediction[0] == 1:
                diab_diagnosis = 'The person is diabetic'
            else:
                diab_diagnosis = 'The person is not diabetic'

            st.success(diab_diagnosis)



##2nd
# Heart Disease Prediction Page
if selected == 'Heart Disease Prediction':

    # page title
    st.title('Heart Disease Prediction using ML')

    col1, col2, col3 = st.columns(3)

    with col1:
        age = st.number_input(
            "Age (years)", 
            min_value=0, 
            max_value=100, 
            step=1, 
            format="%d", 
            help="Normal range: 0-100 years. Type or use buttons."
        )

    with col2:
         sex = st.selectbox(
            "Sex",
            options=[0, 1],
            format_func=lambda x: "Female" if x == 0 else "Male",
            help="0 = Female, 1 = Male"
        )

            

    with col3:
        cp = st.selectbox(
            "Chest Pain Type",
            options=[0, 1, 2, 3],
            format_func=lambda x: {
                0: "Typical Angina", 
                1: "Atypical Angina", 
                2: "Non-anginal Pain", 
                3: "Asymptomatic"
            }.get(x),
            help="Types of chest pain: 0 = Typical Angina, 1 = Atypical Angina, 2 = Non-anginal Pain, 3 = Asymptomatic"
        )

    with col1:
        trestbps = st.number_input(
            "Resting Blood Pressure (mmHg)", 
            min_value=80, 
            max_value=200, 
            step=1, 
            format="%d", 
            help="Normal range: 90-120 mmHg. Type or use buttons."
        )

    with col2:
        chol = st.number_input(
            "Serum Cholesterol (mg/dl)", 
            min_value=100, 
            max_value=600, 
            step=1, 
            format="%d", 
            help="Normal range: 125-200 mg/dl. Type or use buttons."
        )

    with col3:
        fbs = st.selectbox(
            "Fasting Blood Sugar > 120 mg/dl",
            options=[0, 1],
            format_func=lambda x: "No" if x == 0 else "Yes",
            help="0 = False (≤120 mg/dl), 1 = True (>120 mg/dl)"
        )

    with col1:
        restecg = st.selectbox(
            "Resting Electrocardiographic Results",
            options=[0, 1, 2],
            format_func=lambda x: {
                0: "Normal", 
                1: "ST-T Wave Abnormality", 
                2: "Left Ventricular Hypertrophy"
            }.get(x),
            help="0 = Normal, 1 = ST-T Wave Abnormality, 2 = Left Ventricular Hypertrophy"
        )

    with col2:
        thalach = st.number_input(
            "Maximum Heart Rate Achieved (bpm)", 
            min_value=60, 
            max_value=220, 
            step=1, 
            format="%d", 
            help="Normal range: 60-220 bpm. Type or use buttons."
        )

    with col3:
        exang = st.selectbox(
            "Exercise Induced Angina",
            options=[0, 1],
            format_func=lambda x: "No" if x == 0 else "Yes",
            help="0 = No, 1 = Yes"
        )

    with col1:
        oldpeak = st.number_input(
            "ST Depression Induced by Exercise", 
            min_value=0.0, 
            max_value=10.0, 
            step=0.1, 
            format="%.1f", 
            help="ST depression relative to rest. Normal range: 0-6.2. Type or use buttons."
        )

    with col2:
        slope = st.selectbox(
            "Slope of Peak Exercise ST Segment",
            options=[0, 1, 2],
            format_func=lambda x: {
                0: "Upsloping", 
                1: "Flat", 
                2: "Downsloping"
            }.get(x),
            help="0 = Upsloping, 1 = Flat, 2 = Downsloping"
        )

    with col3:
        ca = st.selectbox(
            "Major Vessels Colored by Fluoroscopy",
            options=[0, 1, 2, 3, 4],
            help="Number of major vessels (0-4) colored by fluoroscopy"
        )

    with col1:
        thal = st.selectbox(
            "Thalassemia",
            options=[0, 1, 2, 3],
            format_func=lambda x: {
                0: "Normal", 
                1: "Fixed Defect", 
                2: "Reversible Defect",
                3: "Unknown"
            }.get(x),
            help="0 = Normal, 1 = Fixed Defect, 2 = Reversible Defect, 3 = Unknown"
        )
    # code for Prediction
    heart_diagnosis = ''

    # creating a button for Prediction

    if st.button('Heart Disease Test Result'):

        user_input = [age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]

        user_input = [float(x) for x in user_input]

         # Uses the models to make predictions based on the inputs.
        heart_prediction = heart_disease_model.predict([user_input])

        if heart_prediction[0] == 1:
            heart_diagnosis = 'The person is having heart disease'
        else:
            heart_diagnosis = 'The person does not have heart disease'

    st.success(heart_diagnosis)


# 3rd
# Parkinson's Prediction Page
# if selected == "Parkinsons Prediction":

#     # page title
#     st.title("Parkinson's Disease Prediction using ML")

#     col1, col2, col3, col4, col5 = st.columns(5)

#     with col1:
#         fo = st.text_input('MDVP:Fo(Hz)')

#     with col2:
#         fhi = st.text_input('MDVP:Fhi(Hz)')

#     with col3:
#         flo = st.text_input('MDVP:Flo(Hz)')

#     with col4:
#         Jitter_percent = st.text_input('MDVP:Jitter(%)')

#     with col5:
#         Jitter_Abs = st.text_input('MDVP:Jitter(Abs)')

#     with col1:
#         RAP = st.text_input('MDVP:RAP')

#     with col2:
#         PPQ = st.text_input('MDVP:PPQ')

#     with col3:
#         DDP = st.text_input('Jitter:DDP')

#     with col4:
#         Shimmer = st.text_input('MDVP:Shimmer')

#     with col5:
#         Shimmer_dB = st.text_input('MDVP:Shimmer(dB)')

#     with col1:
#         APQ3 = st.text_input('Shimmer:APQ3')

#     with col2:
#         APQ5 = st.text_input('Shimmer:APQ5')

#     with col3:
#         APQ = st.text_input('MDVP:APQ')

#     with col4:
#         DDA = st.text_input('Shimmer:DDA')

#     with col5:
#         NHR = st.text_input('NHR')

#     with col1:
#         HNR = st.text_input('HNR')

#     with col2:
#         RPDE = st.text_input('RPDE')

#     with col3:
#         DFA = st.text_input('DFA')

#     with col4:
#         spread1 = st.text_input('spread1')

#     with col5:
#         spread2 = st.text_input('spread2')

#     with col1:
#         D2 = st.text_input('D2')

#     with col2:
#         PPE = st.text_input('PPE')

#     # code for Prediction
#     parkinsons_diagnosis = ''

#     # creating a button for Prediction    
#     if st.button("Parkinson's Test Result"):

#         user_input = [fo, fhi, flo, Jitter_percent, Jitter_Abs,
#                       RAP, PPQ, DDP,Shimmer, Shimmer_dB, APQ3, APQ5,
#                       APQ, DDA, NHR, HNR, RPDE, DFA, spread1, spread2, D2, PPE]

#         user_input = [float(x) for x in user_input]

#          # Uses the models to make predictions based on the inputs.
#         parkinsons_prediction = parkinsons_model.predict([user_input])

#         if parkinsons_prediction[0] == 1:
#             parkinsons_diagnosis = "The person has Parkinson's disease"
#         else:
#             parkinsons_diagnosis = "The person does not have Parkinson's disease"

#     st.success(parkinsons_diagnosis)
