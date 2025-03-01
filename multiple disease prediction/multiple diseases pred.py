import streamlit as st
import numpy as np
from PIL import Image
import pickle
from streamlit_option_menu import option_menu

# Load models
diabetes_model = pickle.load(open("C:/Users/bipin/OneDrive/Desktop/Mini Project/saved models/diabetes_model.sav", 'rb'))
heart_disease_model = pickle.load(open("C:/Users/bipin/OneDrive/Desktop/Mini Project/saved models/heart_disease_model.sav", 'rb'))
parkinsons_model = pickle.load(open("C:/Users/bipin/OneDrive/Desktop/Mini Project/saved models/parkinsons_model.sav", 'rb'))
Breast_Cancer_model = pickle.load(open("C:/Users/bipin/OneDrive/Desktop/Mini Project/saved models/breast_cancer.sav", 'rb'))

# Custom CSS for background and font
st.markdown("""
    <style>
    .reportview-container {
        background: #f0f2f6;
        color: #31333f;
    }
    .sidebar .sidebar-content {
        background: #3e3f47;
    }
    .stButton>button {
        color: white;
        background-color: #4caf50;
    }
    .stTextInput>div>div>input {
        font-size: 16px;
        color: #3a3a3a;
    }
    .stMarkdown h1, .stMarkdown h2 {
        color: #2c3e50;
    }
    </style>
""", unsafe_allow_html=True)

# Sidebar for navigation
with st.sidebar:
    selected = option_menu('Multiple Disease Prediction System',
                           ['Diabetes Prediction', 'Heart Disease Prediction', 'Parkinsons Prediction', 'Breast Cancer Prediction'],
                           icons=['activity', 'heart', 'person', 'medkit'],
                           default_index=0)

# Diabetes Prediction Page
if selected == 'Diabetes Prediction':
    st.title('Diabetes Prediction using Machine Learning 🩺')
    img1 = Image.open('C:/Users/bipin/Downloads/di.png')
    st.image(img1, caption="Stay Healthy, Stay Safe", use_column_width=True)

    # Form layout with input handling
    st.markdown("### Please enter your details below:")
    col1, col2, col3 = st.columns(3)

    with col1:
        Pregnancies = st.number_input('Number of Pregnancies (Range: 0-17) [Normal: 0-5, High: 6+]', min_value=0, max_value=17, value=1, step=1)
        
    with col2:
        Glucose = st.number_input('Glucose Level (Range: 70-200) [Normal: 70-100, High: >140]', min_value=70, max_value=200, value=100)
        
    with col3:
        BloodPressure = st.number_input('Blood Pressure (Range: 70-180) [Normal: 80-120, High: >130]', min_value=70, max_value=180, value=120)
    
    with col1:
        SkinThickness = st.number_input('Skin Thickness (Range: 10-100) [Normal: 10-40, High: >50]', min_value=10, max_value=100, value=20)
    
    with col2:
        Insulin = st.number_input('Insulin Level (Range: 0-900) [Normal: 16-166, High: >200]', min_value=0, max_value=900, value=100)
    
    with col3:
        BMI = st.number_input('BMI Value (Range: 15.0-60.0) [Normal: 18.5-24.9, High: >30]', min_value=15.0, max_value=60.0, value=25.0)
    
    with col1:
        DiabetesPedigreeFunction = st.number_input('Diabetes Pedigree Function (Range: 0.0-2.5) [Normal: 0.2-0.8]', min_value=0.0, max_value=2.5, value=0.5)
    
    with col2:
        Age = st.number_input('Age (Range: 0-120) [Normal: 20-60, High: >60]', min_value=0, max_value=120, value=25)

    # Prediction and precautions
    diab_diagnosis = ''
    if st.button('Predict Diabetes'):
        diab_prediction = diabetes_model.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])
        if diab_prediction[0] == 1:
            diab_diagnosis = 'The person is diabetic 🩸'
        else:
            diab_diagnosis = 'The person is not diabetic 🟢'
    st.success(diab_diagnosis)

    st.markdown("### Preventive Measures for Diabetes 🛡️")
    st.write("""
    - **Healthy Diet:** Choose low-sugar foods.
    - **Exercise Regularly:** Aim for 30 minutes daily.
    - **Routine Check-ups:** Regular health checkups are crucial.
    """)

# Heart Disease Prediction Page
if selected == 'Heart Disease Prediction':
    st.title('Heart Disease Prediction using Machine Learning ❤️')
    img2 = Image.open('C:/Users/bipin/Downloads/si.png')
    st.image(img2, use_column_width=True)

    st.markdown("### Please enter the following details:")
    col1, col2, col3 = st.columns(3)

    with col1:
        age = st.number_input('Age (Range: 0-120) [Normal: 20-60, High: >60]', min_value=0, max_value=120, value=30)

    with col2:
        sex = st.selectbox('Sex', [1, 0], format_func=lambda x: 'Male' if x == 1 else 'Female')

    with col3:
        cp = st.selectbox('Chest Pain Type', [0, 1, 2, 3], format_func=lambda x: ['Asymptomatic', 'Typical Angina', 'Atypical Angina', 'Non-Anginal Pain'][x])

    with col1:
        trestbps = st.number_input('Resting Blood Pressure (Range: 50-200) [Normal: 80-120, High: >130]', min_value=50, max_value=200, value=120)

    with col2:
        chol = st.number_input('Serum Cholesterol (Range: 100-500) [Normal: 150-200, High: >240]', min_value=100, max_value=500, value=200)

    with col3:
        fbs = st.selectbox('Fasting Blood Sugar > 120 mg/dl', [1, 0], format_func=lambda x: 'Yes' if x == 1 else 'No')

    with col1:
        restecg = st.selectbox('Resting ECG Results', [0, 1, 2])

    with col2:
        thalach = st.number_input('Maximum Heart Rate Achieved (Range: 50-200) [Normal: 60-100]', min_value=50, max_value=200, value=150)

    with col3:
        exang = st.selectbox('Exercise Induced Angina', [0, 1], format_func=lambda x: 'No' if x == 0 else 'Yes')

    with col1:
        oldpeak = st.number_input('ST Depression Induced by Exercise (Range: 0.0-6.0) [Normal: 0.0-1.0]', min_value=0.0, max_value=6.0, value=1.0)

    with col2:
        slope = st.selectbox('Slope of the Peak Exercise ST Segment', [0, 1, 2])

    with col3:
        ca = st.number_input('Number of Major Vessels Colored by Fluoroscopy (Range: 0-3) [Normal: 0-1]', min_value=0, max_value=3, value=0)

    with col1:
        thal = st.selectbox('Thalassemia', [0, 1, 2], format_func=lambda x: ['Normal', 'Fixed Defect', 'Reversible Defect'][x])

    # Heart Disease Prediction
    heart_diagnosis = ''
    if st.button('Predict Heart Disease'):
        input_data = np.array([[age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]])
        heart_prediction = heart_disease_model.predict(input_data)
        if heart_prediction[0] == 1:
            heart_diagnosis = 'The person has heart disease 💔'
        else:
            heart_diagnosis = 'The person does not have heart disease 💖'
    st.success(heart_diagnosis)

    st.markdown("### Preventive Measures for Heart Disease 💡")
    st.write("""
    - **Balanced Diet:** Reduce saturated fats.
    - **Physical Activity:** 30 minutes daily.
    - **Quit Smoking:** Improve your heart health instantly.
    """)

# Add similar layouts for Parkinson's and Breast Cancer as needed...

# Parkinson's Prediction Page
# Parkinson's Prediction Page


if selected == "Parkinsons Prediction":
    img4 = Image.open('C:/Users/bipin/Downloads/park.png')
   
    
    # Page title with some styling
    st.markdown("<h1 style='text-align: center; color: #4CAF50;'>Parkinson's Disease Prediction using ML</h1>", unsafe_allow_html=True)
    st.image(img4, caption="Stay Healthy, Stay Safe", use_column_width=True)
    st.markdown("<p style='text-align: center;'>Fill in the parameters below to predict the likelihood of Parkinson's disease.</p>", unsafe_allow_html=True)

    # Add a description or instructions
    st.markdown("<p style='text-align: center;'>The input features are based on voice measurements. Use the sliders to input values within recommended ranges.</p>", unsafe_allow_html=True)

    # Dividing input fields into columns and using sliders for better UX with range limits
    st.markdown("### Voice Measurements")
    col1, col2, col3, col4, col5 = st.columns(5)
    
    with col1:
        fo = st.slider('MDVP:Fo(Hz)', min_value=50.0, max_value=300.0, value=120.0, step=1.0, help="Fundamental frequency of voice (range: 50-300 Hz)")
        
    with col2:
        fhi = st.slider('MDVP:Fhi(Hz)', min_value=100.0, max_value=400.0, value=200.0, step=1.0, help="Maximum vocal fundamental frequency (range: 100-400 Hz)")
        
    with col3:
        flo = st.slider('MDVP:Flo(Hz)', min_value=50.0, max_value=300.0, value=100.0, step=1.0, help="Minimum vocal fundamental frequency (range: 50-300 Hz)")
        
    with col4:
        Jitter_percent = st.slider('MDVP:Jitter(%)', min_value=0.0, max_value=1.0, value=0.01, step=0.001, help="Variation in fundamental frequency (range: 0-1%)")
        
    with col5:
        Jitter_Abs = st.slider('MDVP:Jitter(Abs)', min_value=0.0, max_value=0.01, value=0.002, step=0.0001, help="Absolute Jitter (range: 0-0.01)")
        
    with col1:
        RAP = st.slider('MDVP:RAP', min_value=0.0, max_value=0.01, value=0.0025, step=0.0001, help="Relative amplitude perturbation (range: 0-0.01)")
        
    with col2:
        PPQ = st.slider('MDVP:PPQ', min_value=0.0, max_value=0.01, value=0.0025, step=0.0001, help="Five-point period perturbation quotient (range: 0-0.01)")
        
    with col3:
        DDP = st.slider('Jitter:DDP', min_value=0.0, max_value=0.03, value=0.0075, step=0.001, help="Difference of differences of periods (range: 0-0.03)")
        
    with col4:
        Shimmer = st.slider('MDVP:Shimmer', min_value=0.0, max_value=0.1, value=0.01, step=0.001, help="Variation in amplitude (range: 0-0.1)")
        
    with col5:
        Shimmer_dB = st.slider('MDVP:Shimmer(dB)', min_value=0.0, max_value=1.0, value=0.1, step=0.01, help="Shimmer in decibels (range: 0-1 dB)")
        
    with col1:
        APQ3 = st.slider('Shimmer:APQ3', min_value=0.0, max_value=0.05, value=0.015, step=0.001, help="Three-point amplitude perturbation quotient (range: 0-0.05)")
        
    with col2:
        APQ5 = st.slider('Shimmer:APQ5', min_value=0.0, max_value=0.05, value=0.0175, step=0.001, help="Five-point amplitude perturbation quotient (range: 0-0.05)")
        
    with col3:
        APQ = st.slider('MDVP:APQ', min_value=0.0, max_value=0.05, value=0.02, step=0.001, help="Amplitude perturbation quotient (range: 0-0.05)")
        
    with col4:
        DDA = st.slider('Shimmer:DDA', min_value=0.0, max_value=0.15, value=0.05, step=0.005, help="Difference of differences of amplitudes (range: 0-0.15)")
        
    with col5:
        NHR = st.slider('NHR', min_value=0.0, max_value=1.0, value=0.01, step=0.01, help="Noise-to-Harmonics ratio (range: 0-1)")
        
    with col1:
        HNR = st.slider('HNR', min_value=0.0, max_value=50.0, value=20.0, step=1.0, help="Harmonics-to-Noise ratio (range: 0-50)")
        
    with col2:
        RPDE = st.slider('RPDE', min_value=0.0, max_value=1.0, value=0.5, step=0.01, help="Recurrence period density entropy (range: 0-1)")
        
    with col3:
        DFA = st.slider('DFA', min_value=0.0, max_value=1.0, value=0.5, step=0.01, help="Detrended fluctuation analysis (range: 0-1)")
        
    with col4:
        spread1 = st.slider('Spread1', min_value=-10.0, max_value=5.0, value=-5.0, step=0.1, help="Nonlinear measure of fundamental frequency variation (range: -10 to 5)")
        
    with col5:
        spread2 = st.slider('Spread2', min_value=0.0, max_value=0.6, value=0.2, step=0.01, help="Nonlinear measure of fundamental frequency variation (range: 0-0.6)")
        
    with col1:
        D2 = st.slider('D2', min_value=0.0, max_value=4.0, value=2.0, step=0.1, help="Nonlinear dynamical complexity measure (range: 0-4)")
        
    with col2:
        PPE = st.slider('PPE', min_value=0.0, max_value=0.5, value=0.1, step=0.01, help="Pitch period entropy (range: 0-0.5)")
    
    # Code for Prediction
    parkinsons_diagnosis = ''
    
    # Creating a button for Prediction    
    if st.button("Parkinson's Test Result"):
        try:
            # Prediction model takes floats, converting text inputs to float
            parkinsons_prediction = parkinsons_model.predict([[fo, fhi, flo, Jitter_percent, Jitter_Abs, RAP, PPQ, DDP, 
                                                               Shimmer, Shimmer_dB, APQ3, APQ5, APQ, DDA, NHR, HNR, RPDE, 
                                                               DFA, spread1, spread2, D2, PPE]])
            
            if parkinsons_prediction[0] == 1:
                parkinsons_diagnosis = "The person has Parkinson's disease"
            else:
                parkinsons_diagnosis = "The person does not have Parkinson's disease"
                
            st.success(parkinsons_diagnosis)

        except ValueError:
            st.error("Please enter valid numeric values.")



if selected == "Breast Cancer Prediction":
    
    # Title page with a catchy title and subtitle
    st.markdown("<h1 style='text-align: center; color: #4CAF50;'>Breast Cancer Detection Model</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center;'>Predict the likelihood of breast cancer with input features</p>", unsafe_allow_html=True)

    # Add a description or instructions
    st.markdown("<p style='text-align: center;'>Please fill in the details below for an accurate prediction:</p>", unsafe_allow_html=True)

    # Using an expander to hide detailed info if needed
    with st.expander("Input Features"):
        
        # Columns for input fields grouped in a structured format
        st.markdown("### Mean Features")
        col1, col2, col3 = st.columns(3)
        with col1:
            mean_radius = st.number_input('Mean Radius', min_value=6.0, max_value=30.0, value=14.0, format="%.3f", help="Range: 6 - 30")
        with col2:
            mean_texture = st.number_input('Mean Texture', min_value=9.0, max_value=40.0, value=20.0, format="%.3f", help="Range: 9 - 40")
        with col3:
            mean_perimeter = st.number_input('Mean Perimeter', min_value=40.0, max_value=190.0, value=90.0, format="%.3f", help="Range: 40 - 190")
        
        with col1:
            mean_area = st.number_input('Mean Area', min_value=100.0, max_value=2500.0, value=700.0, format="%.3f", help="Range: 100 - 2500")
        with col2:
            mean_smoothness = st.number_input('Mean Smoothness', min_value=0.05, max_value=0.2, value=0.1, format="%.3f", help="Range: 0.05 - 0.2")
        with col3:
            mean_compactness = st.number_input('Mean Compactness', min_value=0.01, max_value=0.35, value=0.15, format="%.3f", help="Range: 0.01 - 0.35")
        
        with col1:
            mean_concavity = st.number_input('Mean Concavity', min_value=0.0, max_value=0.45, value=0.20, format="%.3f", help="Range: 0 - 0.45")
        with col2:
            mean_concave_points = st.number_input('Mean Concave Points', min_value=0.0, max_value=0.25, value=0.1, format="%.3f", help="Range: 0 - 0.25")
        with col3:
            mean_symmetry = st.number_input('Mean Symmetry', min_value=0.1, max_value=0.5, value=0.2, format="%.3f", help="Range: 0.1 - 0.5")
        
        with col1:
            mean_fractal_dimension = st.number_input('Mean Fractal Dimension', min_value=0.05, max_value=0.1, value=0.06, format="%.3f", help="Range: 0.05 - 0.1")
        
        st.markdown("### Error Features")
        col1, col2, col3 = st.columns(3)
        with col1:
            radius_error = st.number_input('Radius Error', min_value=0.1, max_value=3.0, value=0.5, format="%.3f", help="Range: 0.1 - 3.0")
        with col2:
            texture_error = st.number_input('Texture Error', min_value=0.1, max_value=5.0, value=1.0, format="%.3f", help="Range: 0.1 - 5.0")
        with col3:
            perimeter_error = st.number_input('Perimeter Error', min_value=1.0, max_value=25.0, value=5.0, format="%.3f", help="Range: 1 - 25")
        
        with col1:
            area_error = st.number_input('Area Error', min_value=5.0, max_value=550.0, value=40.0, format="%.3f", help="Range: 5 - 550")
        with col2:
            smoothness_error = st.number_input('Smoothness Error', min_value=0.002, max_value=0.04, value=0.01, format="%.3f", help="Range: 0.002 - 0.04")
        with col3:
            compactness_error = st.number_input('Compactness Error', min_value=0.002, max_value=0.14, value=0.03, format="%.3f", help="Range: 0.002 - 0.14")
        
        with col1:
            concavity_error = st.number_input('Concavity Error', min_value=0.0, max_value=0.4, value=0.05, format="%.3f", help="Range: 0 - 0.4")
        with col2:
            concave_points_error = st.number_input('Concave Points Error', min_value=0.0, max_value=0.2, value=0.02, format="%.3f", help="Range: 0 - 0.2")
        with col3:
            symmetry_error = st.number_input('Symmetry Error', min_value=0.01, max_value=0.08, value=0.03, format="%.3f", help="Range: 0.01 - 0.08")
        
        with col1:
            fractal_dimension_error = st.number_input('Fractal Dimension Error', min_value=0.0001, max_value=0.03, value=0.004, format="%.3f", help="Range: 0.0001 - 0.03")
        
        st.markdown("### Worst Features")
        col1, col2, col3 = st.columns(3)
        with col1:
            worst_radius = st.number_input('Worst Radius', min_value=7.0, max_value=40.0, value=16.0, format="%.3f", help="Range: 7 - 40")
        with col2:
            worst_texture = st.number_input('Worst Texture', min_value=12.0, max_value=50.0, value=25.0, format="%.3f", help="Range: 12 - 50")
        with col3:
            worst_perimeter = st.number_input('Worst Perimeter', min_value=50.0, max_value=250.0, value=120.0, format="%.3f", help="Range: 50 - 250")
        
        with col1:
            worst_area = st.number_input('Worst Area', min_value=100.0, max_value=3000.0, value=880.0, format="%.3f", help="Range: 100 - 3000")
        with col2:
            worst_smoothness = st.number_input('Worst Smoothness', min_value=0.05, max_value=0.25, value=0.15, format="%.3f", help="Range: 0.05 - 0.25")
        with col3:
            worst_compactness = st.number_input('Worst Compactness', min_value=0.02, max_value=1.1, value=0.35, format="%.3f", help="Range: 0.02 - 1.1")
        
        with col1:
            worst_concavity = st.number_input('Worst Concavity', min_value=0.0, max_value=1.25, value=0.45, format="%.3f", help="Range: 0 - 1.25")
        with col2:
            worst_concave_points = st.number_input('Worst Concave Points', min_value=0.0, max_value=0.3, value=0.2, format="%.3f", help="Range: 0 - 0.3")
        with col3:
            worst_symmetry = st.number_input('Worst Symmetry', min_value=0.1, max_value=0.7, value=0.3, format="%.3f", help="Range: 0.1 - 0.7")
        
        with col1:
            worst_fractal_dimension = st.number_input('Worst Fractal Dimension', min_value=0.05, max_value=0.15, value=0.09, format="%.3f", help="Range: 0.05 - 0.15")

    # Code for prediction
    breast_cancer_diagnosis = ''

    # Creating a button for prediction
    if st.button('Get Breast Cancer Test Result'):
        
        # Convert all inputs to float as necessary for model prediction
        try:
            input_features = [
                float(mean_radius), float(mean_texture), float(mean_perimeter), float(mean_area),
                float(mean_smoothness), float(mean_compactness), float(mean_concavity),
                float(mean_concave_points), float(mean_symmetry), float(mean_fractal_dimension),
                float(radius_error), float(texture_error), float(perimeter_error), float(area_error),
                float(smoothness_error), float(compactness_error), float(concavity_error),
                float(concave_points_error), float(symmetry_error), float(fractal_dimension_error),
                float(worst_radius), float(worst_texture), float(worst_perimeter), float(worst_area),
                float(worst_smoothness), float(worst_compactness), float(worst_concavity),
                float(worst_concave_points), float(worst_symmetry), float(worst_fractal_dimension)
            ]
        
            breast_cancer_prediction = Breast_Cancer_model.predict([input_features])
            
            if breast_cancer_prediction[0] == 0:
                breast_cancer_diagnosis = 'Breast Cancer is Malignant'
            else:
                breast_cancer_diagnosis = 'Breast Cancer is Benign'

            st.success(breast_cancer_diagnosis)

        except ValueError:
            st.error("Please enter valid numeric values for all inputs.")

    # Breast cancer prevention tips
    with st.expander("Breast Cancer Prevention Tips"):
        st.markdown("""
        - **Maintain a healthy weight**: Obesity can increase the risk of breast cancer.
        - **Exercise regularly**: Physical activity helps regulate hormones that may influence breast cancer risk.
        - **Limit alcohol consumption**: Drinking alcohol is a significant risk factor.
        - **Stay aware of family history**: Early detection can be lifesaving, especially if there is a family history of breast cancer.
        - **Quit smoking**: Smoking is linked to a higher risk of breast cancer, especially in younger women.
        - **Breastfeed if possible**: Breastfeeding for at least several months may lower breast cancer risk.
        - **Regular self-exams and screenings**: Early detection through mammograms and self-exams is critical.
        """)




# Add similar layouts for Parkinson's and Breast Cancer as needed...
