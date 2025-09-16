"""
===============================================
   FastAPI Project: Heart Disease Prediction
   ------------------------------------------
   Author: Muhammad Huzaifa
   Description:
       This FastAPI app demonstrates how to:
       - Build RESTful APIs using FastAPI
       - Validate user input with Pydantic
       - Load a pre-trained ML model with pickle
       - Predict outcomes and return JSON response
===============================================
"""

# ----------------------------
# Importing Required Libraries
# ----------------------------
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
import pickle

# ----------------------------
# Initialize FastAPI App
# ----------------------------
app = FastAPI(
    title="Heart Disease Prediction API",
    description="A simple API that predicts the likelihood of heart disease based on input health parameters.",
    version="1.0.0"
)

# ----------------------------
# Schema Definition with Validation
# ----------------------------
# Pydantic model defines what input data we expect and validates it.
class Item(BaseModel):
    gender: int = Field(..., ge=0, le=1, description="Gender: 1 (Male), 0 (Female)")
    age: int = Field(..., gt=0, description="Age must be greater than 0")
    Education: float = Field(..., gt=0, description="Education level (numeric value)")
    currentSmoker: int = Field(..., ge=0, description="1 if current smoker, else 0")
    cigsPerDay: float = Field(..., ge=0, description="Number of cigarettes smoked per day")
    BPMeds: float = Field(..., ge=0, description="1 if on BP medication, else 0")
    prevalentStroke: int = Field(..., ge=0, description="1 if previously had a stroke, else 0")
    prevalentHyp: int = Field(..., ge=0, description="1 if prevalent hypertension, else 0")
    diabetes: int = Field(..., ge=0, description="1 if diabetic, else 0")
    totChol: float = Field(..., gt=0, description="Total cholesterol level")
    SysBP: float = Field(..., gt=0, description="Systolic Blood Pressure")
    diaBP: float = Field(..., gt=0, description="Diastolic Blood Pressure")
    BMI: float = Field(..., gt=0, description="Body Mass Index")
    HeartRate: float = Field(..., gt=0, description="Heart rate in beats per minute")
    Glucose: float = Field(..., gt=0, description="Blood glucose level")

# ----------------------------
# API Endpoint for Prediction
# ----------------------------
@app.post("/predict/", tags=["Prediction"])
def predict(item: Item):
    """
    Predicts the likelihood of heart disease using a pre-trained model.
    
    Steps:
    1. Validate input data using Pydantic.
    2. Convert input features into a list format for the model.
    3. Load pre-trained ML model from pickle file.
    4. Perform prediction and return result as JSON.
    """

    try:
        # Extract data into dictionary
        features = item.model_dump()

        # Convert dict values into list (model expects a list of values)
        values_list = list(features.values())

        # Load pre-trained model (ensure model file exists in the same folder)
        with open("heartdisease_classification_model.pkl", 'rb') as model_file:
            loaded_model = pickle.load(model_file)

        # Perform prediction (wrap in list for sklearn)
        result = loaded_model.predict([values_list])

        # Return response
        return {
            "msg": "Prediction Successful",
            "Predicted Result": int(result.tolist()[0])  # Convert numpy type to int for JSON
        }

    except FileNotFoundError:
        raise HTTPException(status_code=500, detail="Model file not found. Please ensure the .pkl file exists.")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Prediction failed: {str(e)}")

# ----------------------------
# Run Command:
# uvicorn main:app --reload
# ----------------------------
