import random
import smtplib
import datetime as dt

MY_EMAIL = "jacreighton669@gmail.com"
PASSWORD = "hwaegdrycxwfmmyv"
now = dt.datetime.now()
day_of_week = now.weekday()

with open("quotes.txt") as quote_file:
    quotes = quote_file.readlines()
    quote_today = random.choice(quotes)

if day_of_week == 3:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs="justincreighton2006@gmail.com",
            msg=f"Subject: Happy Thursday\n\n{quote_today}"
        )
