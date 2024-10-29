from fastapi import FastAPI, Query
from pycaret.classification import load_model, predict_model
import pandas as pd
from fastapi.middleware.cors import CORSMiddleware

# Create the app
app = FastAPI()

app.add_middleware(
  CORSMiddleware,
  allow_origins=["*"],  # Allow access from any origin. Restrict in production.
  allow_credentials=True,
  allow_methods=["*"],
  allow_headers=["*"],
)

# Load the trained model
model = load_model("Student_performance_model")

@app.get("/predict")
async def predict(
    Age: int = Query(..., description="Student's age (15 to 18 years)"),
    Gender: int = Query(..., description="Student's gender (0: Male, 1: Female)"),
    Ethnicity: int = Query(..., description="Ethnicity (0: Caucasian, 1: African American, 2: Asian, 3: Other)"),
    ParentalEducation: int = Query(..., description="Parental education level (0: None, 1: High School, 2: Some College, 3: Bachelor's, 4: Higher)"),
    StudyTimeWeekly: float = Query(..., description="Weekly study time (in hours, from 0 to 20)"),
    Absences: int = Query(..., description="Number of absences during the school year (0 to 30)"),
    Tutoring: int = Query(..., description="Receiving tutoring (0: No, 1: Yes)"),
    ParentalSupport: int = Query(..., description="Level of parental support (0: None, 1: Low, 2: Medium, 3: High, 4: Very High)"),
    Extracurricular: int = Query(..., description="Participation in extracurricular activities (0: No, 1: Yes)"),
    Sports: int = Query(..., description="Participation in sports activities (0: No, 1: Yes)"),
    Music: int = Query(..., description="Participation in music activities (0: No, 1: Yes)"),
    Volunteering: int = Query(..., description="Participation in volunteering activities (0: No, 1: Yes)"),
):
    # Collect data in a dictionary
    data = {
        "Age": Age,
        "Gender": Gender,
        "Ethnicity": Ethnicity,
        "ParentalEducation": ParentalEducation,
        "StudyTimeWeekly": StudyTimeWeekly,
        "Absences": Absences,
        "Tutoring": Tutoring,
        "ParentalSupport": ParentalSupport,
        "Extracurricular": Extracurricular,
        "Sports": Sports,
        "Music": Music,
        "Volunteering": Volunteering,
    }
  
    # Convert data to DataFrame
    df = pd.DataFrame([data])
  
    # Make a prediction
    predictions = predict_model(model, data=df)
  
    # Extract prediction
    predicted_grade = predictions["prediction_label"].iloc[0]
    grade_map = {
        0: 'Excellent (90-100%)',
        1: 'Very Good (80-89%)',
        2: 'Good (70-79%)',
        3: 'Satisfactory (60-69%)',
        4: 'Failing (Below 60%)'
    }
    grade = grade_map.get(predicted_grade, 'Unknown')
  
    return {"Predicted Grade": grade}
