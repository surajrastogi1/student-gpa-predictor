🎓 Student GPA Predictor
A Machine Learning-powered web application that predicts a student's GPA based on various demographic, academic, and behavioral factors. This tool is built using Streamlit for the frontend and Scikit-Learn (KNN) for the prediction engine.

🚀 Features
Real-time Prediction: Adjust student metrics via the sidebar and see the predicted GPA instantly.

User-Friendly Interface: Built with Streamlit for a clean, interactive experience.

Comprehensive Metrics: Considers factors like study time, absences, tutoring, and extracurricular activities.

Visual Feedback: Features celebratory effects (balloons) for high predicted scores.

🛠️ Tech Stack
Python (Core Logic)

Streamlit (Web Framework)

Scikit-Learn (Machine Learning Library)

Pandas & Numpy (Data Manipulation)

Joblib (Model Serialization)

📋 Features Used for Prediction
The model analyzes the following inputs:

Demographics: Age, Gender, Ethnicity.

Academic Habits: Weekly Study Time, Absences, Tutoring.

Support & Environment: Parental Education, Parental Support Level.

Activities: Sports, Music, Volunteering, and general Extracurriculars.

⚙️ Installation & Local Setup
Clone the repository:
git clone https://github.com/surajrastogi1/student-gpa-predictor.git
cd student-gpa-predictor

Create a virtual environment (optional but recommended):
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate

Install dependencies:
pip install -r requirements.txt

Run the application:
streamlit run app.py
📂 Project Structure
Plaintext
├── app.py              # Main Streamlit application code
├── knn_model.pkl       # Pre-trained K-Nearest Neighbors model
├── scaler.pkl          # Pickled Scaler for data normalization
├── requirements.txt    # List of required Python packages
└── README.md           # Project documentation
