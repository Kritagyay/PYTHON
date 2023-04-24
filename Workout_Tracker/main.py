import requests
from datetime import datetime
from dotenv import load_dotenv
import os

NOW=datetime.now().strftime("%d%m%Y")
TIME=datetime.now().strftime("%X")


API_ID="ecf4148d"
load_dotenv()

# GENDER=input("Enter your genderr")
# WEIGHT=input("Enter your weight in Kg")
# HEIGHT=input("Enter your height in cm")
# AGE=input("Enter your age")

api_endpoint="https://trackapi.nutritionix.com/v2/natural/exercise"

params={
    "query":input("Tell me what exercise have you done today?"),
    "gender":"male",
    "weight_kg":80,
    "height_cm":172,
    "age":20,
}

headers={
    "x-app-id":API_ID,
    "x-app-key":os.getenv('API_KEY'),
}

responses=requests.post(url=api_endpoint,json=params,headers=headers)
data=responses.json()
# print(data)

sheety_endpoint="https://api.sheety.co/048edbc1ca3f589a750d678b50deeec9/workoutTracker/sheet1"

for exercise in data["exercises"]:
    sheet_inputs = {
        "sheet1": {
            "date": NOW,
            "time": TIME,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

bearer_header={
    "Authorization":"Bearer kjh3aku8ao0aerxczdfaer4er5ins"
    }

sheet_response=requests.post(
    url=sheety_endpoint,
    json=sheet_inputs,
    headers=bearer_header,
)

print(sheet_response.text)