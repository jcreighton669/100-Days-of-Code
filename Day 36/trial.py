import requests

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
ALPHA_API_KEY = "TMRARY1TXMF4GQ5A"
COMPANY_NAME = "Cisco Systems"
NEWS_API_KEY = "ec719b9a2dc743a784539cd885348d83"


stock_parameters = {
    "function": "TIME_SERIES_DAILY_ADJUSTED",
    "symbol": "CSCO",
    "datatype": "json",
    "apikey": ALPHA_API_KEY
}

news_parameters = {
    "q": COMPANY_NAME,
    "apiKey": NEWS_API_KEY
}

stock_response = requests.get(url=STOCK_ENDPOINT, params=stock_parameters)
stock_response.raise_for_status()

news_response = requests.get(url=NEWS_ENDPOINT, params=news_parameters)
news_response.raise_for_status()


# stock_data_list = [value for (key, value) in data.items()]
news_data = news_response.json()["articles"]
news_data_list = [value for (key, value) in news_data.items()]
print(news_data_list)