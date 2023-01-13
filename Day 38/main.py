import requests
from datetime import datetime

APP_ID = "61489a72"
API_KEY = "eb608d02c9714408b1c97a46004badbd"
GENDER = "male"
WEIGHT_KG = 86.1826
HEIGHT_CM = 167.64
AGE = 34

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY
}

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheety_endpoint = "https://api.sheety.co/7d6aad94864a838a7fc7a9b98a0f2345/workoutTracking/workouts"
exercise_prompt = input("Tell me which exercises you did: ")

params = {
    "query": exercise_prompt,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

response = requests.post(url=exercise_endpoint, json=params, headers=headers)
result = response.json()

today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    sheet_response = requests.post(url=sheety_endpoint, json=sheet_inputs)

    print(sheet_response.text)