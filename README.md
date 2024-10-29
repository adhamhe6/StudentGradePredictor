# 🎓 Student Grade Predictor API

Welcome to the **Student Grade Predictor** API! This project utilizes a trained machine learning model to predict students' final grades based on various demographic, educational, and extracurricular factors. Designed to be practical and efficient, the API can serve as a valuable tool for educational research and student performance analysis.

---

## 🚀 Features
- **FastAPI Backend**: Powered by FastAPI for high-performance asynchronous API calls.
- **Real-time Predictions**: Provides grade predictions based on custom user inputs.
- **Clean and Interactive UI**: Includes a responsive, user-friendly HTML interface.
- **Flexible Input**: Predicts grades based on various factors like age, gender, study time, and extracurricular activities.

---

## 🛠️ Setup Instructions

1. **Clone the repository**
   ```bash
   git clone https://github.com/adhamhe6/StudentGradePredictor.git
   cd StudentGradePredictor
   ```
2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```
3. **Start the API server**
   ```bash
   uvicorn Student_performance_api:app --reload
   ```
The API will be available at [`http://127.0.0.1:8000`](http://127.0.0.1:8000).

---

## 💻 Usage

### Access the HTML Interface
Open `index.html` in your web browser or visit [http://127.0.0.1:8000](http://127.0.0.1:8000) to access the API and its form-based interface.

### Input Parameters
Provide student information such as:

- Age, Gender, Ethnicity
- Parental Education Level
- Study Time, Absences, Tutoring
- Participation in Extracurriculars, Sports, Music, and Volunteering

### Get Predictions
Click **"Predict Grade"** to receive the student's predicted grade based on the provided inputs.

---

## 📈 Model Training

The model is trained using `train.py`, which loads data from `Student_performance_data.csv`, preprocesses it, and trains a PyCaret model. The trained model is saved as `Student_performance_model.pkl`.

To retrain the model:

```bash
python train.py
```  

Happy Predicting! 🎉