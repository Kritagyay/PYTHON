import requests
import datetime
import smtplib
import time

My_Email="rk0475220@gmail.com"
My_Password="zbulhhcxxqeqahnn"
my_lat=float(30.681621)
my_long=float(75.683103)
current=datetime.datetime.now()

def is_overhead():
    response=requests.get(url="https://api.sunrise-sunset.org/json",params=parameters)
    response.raise_for_status()
    data=response.json()

    iss_lat=float(data["iss+position"]["latitude"])
    iss_long=float(data["iss_position"]["longitude"])
    if my_lat-5 <= iss_lat <= my_lat+5 and my_long-5 <= iss_long<= my_long+5:
        return True

def iss_night():
    parameters={
        "lat":my_lat,
        "long":my_long,
        "formatted":0
    }
    response=requests.get(url="https://api.sunrise-sunset.org/json",params=parameters)
    response.raise_for_status()
    data=response.json()

    sunrise=int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset=int(data["results"]["sunset"].split("T")[1].split(":")[0])
    hour=current.hour
    if hour>sunset or hour<sunrise:
        return True

while True:
    time.sleep(60)

    if is_overhead and iss_night:
        connection=smtplib.SMTP("smtp.gmail.com")
        connection.starttls()
        connection.login(My_Email,My_Password)
        connection.sendmail(from_addr=My_Email,to_addrs=My_Email,
                            msg="Subject:ISS IS OVERHEAD\n\n Please go "
                                "outside watch ISS satelite is above you, can you spot it!")