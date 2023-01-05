import requests

OWM_ENDPOINT = "https://pro.openweathermap.org/data/2.5/forecast/hourly"
API_KEY = "6c16d02f47bcaf492608b9c673538eda"

parameters = {
    "lat": 36.031930,
    "lon": -78.454735,
    "appid": "3f72781be7630cf961d771bb5e5077da"
}

response = requests.get(
    url=OWM_ENDPOINT,
    params=parameters
)
response.raise_for_status()

print(response.json())