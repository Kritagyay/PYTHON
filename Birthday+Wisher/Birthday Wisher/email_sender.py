import smtplib

my_email="rk0475220@gmail.com"
password="iydwreqaltdhyvxe"

with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=my_email,password=password)
    connection.sendmail(
        from_addr=my_email,
        to_addrs="2140123@sliet.ac.in",
        msg="Subject: Important mail \n\n This mail is to verify your account."
    )
