import requests
import json
import os
from twilio.rest import Client



api_key="69f04e4613056b159c2761a9d9e664d2"

weather_parameters={
    "lat" : 30.245,
    "lon" :75.842,
    "exclude":"current,minutely,daily",
    "appid":api_key,
}

responses=requests.get(url=f"https://api.openweathermap.org/data/2.5/onecall",params=weather_parameters)
responses.raise_for_status()
data=responses.json()
weather_data=data["hourly"][:12]

will_rain=False

for hour_data in weather_data:
    condition_code=hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain=True

if will_rain:
    account_sid = os.environ['AC178918cf254b1241ab1e05fba94e2de5']
    auth_token = os.environ['4ac207daf85b75815f74aa03031d29e4']
    client = Client(account_sid, auth_token)

    message = client.messages \
        .create(
        body="Please Bring your Umbrella, weather is not clear.",
        from_='+14406414438',
        to='+919506846608'
    )

    print(message.status)