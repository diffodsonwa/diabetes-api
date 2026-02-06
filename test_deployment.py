import requests
import urllib3
urllib3.disable_warnings()  

api_url = "https://diabetes-api.qiow.onrender.com"

test_patient = {
    "Pregnancies": 6,
    "Glucose": 148,
    "BloodPressure": 72,
    "skinThickness": 35,
    "Insulin": 0,
    "BMI": 33.6,
    "DiabetesPedigreeFunction": 0.62,
    "Age": 50 
}

# Add verify=False to bypass SSL check
response = requests.post(
    f"{api_url}/diabetes_prediction",
    json=test_patient,
    verify=False  
)

print("status code:", response.status_code)
print("Response:", response.json())
