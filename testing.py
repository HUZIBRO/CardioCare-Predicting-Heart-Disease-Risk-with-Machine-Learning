"""
Example Client Script to Test the API
-------------------------------------
Run this in a separate Python file after starting the FastAPI server.
"""

import requests

# API URL (make sure FastAPI is running locally on port 8000)
url = "http://127.0.0.1:8000/predict/"

# Example Input Data
loader = {
    'gender': 1,
    'age': 33,
    'Education': 1.0,
    'currentSmoker': 1,
    'cigsPerDay': 4,
    'BPMeds': 0,
    'prevalentStroke': 0,
    'prevalentHyp': 1,
    'diabetes': 0,
    'totChol': 211.4,
    'SysBP': 144.6,
    'diaBP': 95.6,
    'BMI': 29.6,
    'HeartRate': 77.0,
    'Glucose': 85.1
}

# Send POST request to API
resp = requests.post(url, json=loader)

# Print JSON Response
print(resp.json())
