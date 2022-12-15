import smtplib
import datetime as dt

MY_EMAIL = "jacreighton669@gmail.com"
PASSWORD = "hwaegdrycxwfmmyv"
now = dt.datetime.now()
day = now.day
month = now.month

with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=MY_EMAIL, password=PASSWORD)
    connection.sendmail(
        from_addr=MY_EMAIL,
        to_addrs="justincreighton2006@gmail.com",
    )