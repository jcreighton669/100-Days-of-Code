import requests
from datetime import datetime

MY_LATITUDE = 36.032143
MY_LONGITUDE = -78.454788

parameters = {
    "lat": MY_LATITUDE,
    "lng": MY_LONGITUDE,
    "formatted": 0
}

response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()

data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0]) - 5
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0]) - 5

print(sunrise)
print(sunset)

time_now = datetime.now()

print(time_now)