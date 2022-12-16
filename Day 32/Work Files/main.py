# import smtplib
#
# my_email = "jacreighton669@gmail.com"
# password = "hwaegdrycxwfmmyv"
#
# with smtplib.SMTP("smtp.gmail.com") as connection:
#     connection.starttls()
#     connection.login(user=my_email, password=password)
#     connection.sendmail(
#         from_addr=my_email,
#         to_addrs="justincreighton2006@gmail.com",
#         msg="Subject:Hello\n\nThis is the body of my email"
#     )

import datetime as dt
import random

now = dt.datetime.now()
year = now.year
month = now.month
day_of_week = now.weekday()
print(day_of_week)

date_of_birth = dt.datetime(year=1988, month=8, day=10)
print(date_of_birth)


for i in range(50):
    print(random.randint(1, 3))
