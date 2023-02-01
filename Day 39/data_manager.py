import requests
from pprint import pprint

SHEET_API_ENDPOINT = "https://api.sheety.co/7d6aad94864a838a7fc7a9b98a0f2345/flightDeals/prices"


class DataManager:
    def __init__(self):
        self.destination_data = {}

    def get_destination_data(self):
        response = requests.get(url=SHEET_API_ENDPOINT)
        data = response.json()
        self.destination_data = data["prices"]
        return self.destination_data

    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                url=f"{SHEET_API_ENDPOINT}/{city['id']}",
                json=new_data
            )
            print(response.text)
