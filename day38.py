#day 38
# Workout tracking with google sheets


import os
import requests
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()

NUTRITIONIX_API_KEY = os.getenv('NUTRITIONIX_API_KEY')
NUTRITIONIX_API_ID = os.getenv('NUTRITIONIX_API_ID')
NUTR_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise" 
SHEET_ENDPOINT= os.getenv('SHEET_ENDPOINT')
SHEET_API= os.getenv('SHEET_API')


GENDER = "FEMALE" 
WEIGHT_KG = 43 
HEIGHT_CM = 147 
AGE = 26


exercises_user = input("Tell me which exercises you did: ")
headers = { 
    "x-app-id": NUTRITIONIX_API_ID, 
    "x-app-key": NUTRITIONIX_API_KEY, 
    }

parameter = { 
    "query": exercises_user, 
    "gender": GENDER, 
    "weight_kg": WEIGHT_KG, 
    "height_cm": HEIGHT_CM, 
    "age": AGE 
    }

response = requests.post(url=NUTR_ENDPOINT, json=parameter,  headers=headers) 
response.raise_for_status()
data = response.json()

for param in data["exercises"]:
    today_date = datetime.now().strftime("%d/%m/%Y")
    now_time = datetime.now().strftime("%X")

    sheet_paramters = {
        "workout":{
            "date":today_date,
            "time": now_time,
            "exercise":param["name"].title(),
            "duration":param["duration_min"],
            "calories":param["nf_calories"],
        }
    }

    headers = {
        "Authorization": SHEET_API
        }

    response = requests.post(SHEET_ENDPOINT, json=sheet_paramters, headers=headers) 
    response.raise_for_status()
    print(response.text)
