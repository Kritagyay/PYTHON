import smtplib
import random
import datetime as dt
import pandas as pd

My_email="rk0475220@gmail.com"
passcode="zmcnnyvhlsyrixux"

data=pd.read_csv("birthdays.csv")

today=(dt.datetime.now().day,dt.datetime.now().month)

birthday_dict={(data_row["month"],data_row["day"]): data_row for (index,data_row) in data.iterrows()}

if today in birthday_dict:
    birthday_person=birthday_dict[today]
    with open (f"letter_templates/letter_{random.randint(1,3)}.txt") as letter_files:
        content=letter_files.read()
        content.replace("[Name]",birthday_person.name)

    with smtplib.SMTP("smtp.gmail.com") as connections:
        connections.starttls()
        connections.login(My_email,passcode)
        connections.sendmail(from_addr=My_email,
                             to_addrs=birthday_dict["email"],
                             msg=f"Subject:Happy Birthday \n\n {content}")