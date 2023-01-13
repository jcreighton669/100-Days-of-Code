import requests
import datetime as dt

STOCK_NAME = "CSCO"
COMPANY_NAME = "Cisco Systems"
API_KEY = "TMRARY1TXMF4GQ5A"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"

parameters = {
    "function": "TIME_SERIES_DAILY_ADJUSTED",
    "symbol": STOCK_NAME,
    "apikey": API_KEY
}

response = requests.get(url=STOCK_ENDPOINT, params=parameters)
response.raise_for_status()

dt_now = dt.datetime.now()
dt_yesterday = dt_now.date()
print(dt_yesterday)

stock_data_yesterday = response.json()["Time Series (Daily)"]
print()
