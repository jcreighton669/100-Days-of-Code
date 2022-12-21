import smtplib
import time

import requests
from datetime import datetime

MY_LAT = 36.032143  # Your latitude
MY_LONG = -78.454788  # Your longitude
MY_EMAIL = "jacreighton669@gmail.com"
PASSWORD = "hwaegdrycxwfmmyv"


# Your position is within +5 or -5 degrees of the ISS position.
def is_within_range():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])
    if (MY_LAT - 5) <= iss_latitude <= (MY_LAT + 5) and (MY_LONG - 5) <= iss_longitude <= (MY_LONG + 5):
        return True


def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0]) - 5
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0]) - 5

    time_now = datetime.now()

    if time_now >= sunset or time_now <= sunrise:
        return True


while True:
    time.sleep(60)
    if is_within_range() and is_night():
        with smtplib.SMTP("smtp.google.com") as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs="justincreighton2006@gmail.com",
                msg=f"Subject:Look Up👆\n\nThe ISS is above you in the sky!"
            )
# BONUS: run the code every 60 seconds.
