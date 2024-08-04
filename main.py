import requests
from requests.auth import HTTPBasicAuth    #---- For bearer authentication
from datetime import datetime

GENDER = "male"
WEIGHT = 65
HEIGHT = 180
AGE = 18


# ----------Credintials_data--------------

API_KEY = "Your api key"
APP_ID = "Your app id"
AUTH_TOKEN = "Your auth token"
username = "username"
password = "password"

# ---------------------------------------

NUTRITIONIX_ENPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"
SHEET_ENPOINT = "Your sheety enpoint"


headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
    "Content-Type":"application/json"
}

excercise_text = input("Tell me which exercise you did: ")

parameters = {
    "query": excercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT,
    "height_cm": HEIGHT,
    "age": AGE
}

response = requests.post(NUTRITIONIX_ENPOINT, json=parameters, headers=headers)
# response.raise_for_status()
result = response.json()


header = {
    "Authorization": AUTH_TOKEN
}

today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise":exercise["name"].title(),
            "duration":exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

sheet_response = requests.post(SHEET_ENPOINT, json=sheet_inputs, auth=(username, password,))
print(sheet_response.text)