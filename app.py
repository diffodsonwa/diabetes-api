from fastapi import FastAPI
from pydantic import BaseModel
import pickle
import numpy as np  

app = FastAPI()

class ModelInput(BaseModel):
    Pregnancies: int
    Glucose: int
    BloodPressure: int
    skinThickness: int
    Insulin: int
    BMI: float
    DiabetesPedigreeFunction: float
    Age: int

# Load model
diabetes_model = pickle.load(open('diabetes_model.sav', 'rb'))

# ===== ADD THESE ENDPOINTS =====

@app.get("/")
def root():
    """Root endpoint - shows API is working"""
    return {
        "message": "Diabetes Prediction API",
        "status": "active",
        "main_endpoint": "POST /diabetes_prediction",
        "documentation": "/docs or /redoc",
        "health_check": "/health"
    }

@app.get("/health")
def health_check():
    """Health check endpoint for monitoring"""
    return {
        "status": "healthy",
        "service": "diabetes-api",
        "model_loaded": diabetes_model is not None
    }

@app.post('/diabetes_prediction')
def diabetes_pred(input_parameters: ModelInput):
    input_dict = input_parameters.dict()

    # Extract values in correct order
    input_list = [
        input_dict['Pregnancies'],
        input_dict['Glucose'],
        input_dict['BloodPressure'],
        input_dict['skinThickness'],
        input_dict['Insulin'],
        input_dict['BMI'],
        input_dict['DiabetesPedigreeFunction'],
        input_dict['Age']
    ]

    # ✅ CRITICAL FIX: Convert to 2D numpy array
    input_array = np.array(input_list).reshape(1, -1)

    # Make prediction
    prediction = diabetes_model.predict(input_array)

    if prediction[0] == 0:
        return {'prediction': 'The person is not diabetic'}
    else:
        return {'prediction': 'The person is diabetic'}

# ===== DEPLOYMENT SETTINGS =====
if __name__ == "__main__":
    import uvicorn
    import os
    
    # Get port from environment variable (Render sets this)
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)
