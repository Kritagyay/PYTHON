import smtplib
import datetime as dt
import random

my_email="rk0475220@gmail.com"
passcode="wfmkdmtgrltrsxra"

now=dt.datetime.now()
weekday=now.weekday()
if weekday==6:
    with open ("quotes.txt") as txt:
        all_quotes=txt.readlines()
        quote=random.choice(all_quotes)

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(my_email,passcode)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="shubhamsinghmau2@gmail.com",
            msg=f"Subject:Sunday Quote \n\n {quote}"
        )
