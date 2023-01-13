import requests
from twilio.rest import Client

STOCK_NAME = "CSCO"
COMPANY_NAME = "Cisco Systems"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

STOCK_API_KEY = "TMRARY1TXMF4GQ5A"
NEWS_API_KEY = "ec719b9a2dc743a784539cd885348d8"

TWILIO_ACCT_ID = "ACb22d8935c06d47d6a14c27d8ab672c6"
TWILIO_AUTH_TOKEN = "bb2bb9f0d8e7ca722294ecd6c0a1171"

stock_parameters = {
    "function": "TIME_SERIES_DAILY_ADJUSTED",
    "symbol": STOCK_NAME,
    "datatype": "json",
    "apikey": STOCK_API_KEY
}

news_parameters = {
    "qInTitle": COMPANY_NAME,
    "apiKey": NEWS_API_KEY
}

stock_response = requests.get(url=STOCK_ENDPOINT, params=stock_parameters)
stock_response.raise_for_status()

stock_data = stock_response.json()["Time Series (Daily)"]
stock_data_list = [value for (key, value) in stock_data.items()]
yesterday_data = stock_data_list[0]
yesterday_closing_price = float(yesterday_data["4. close"])
print(yesterday_closing_price)

day_before_yesterday_data = stock_data_list[1]
day_before_yesterday_closing_price = float(day_before_yesterday_data["4. close"])
print(day_before_yesterday_closing_price)

difference = abs(day_before_yesterday_closing_price - yesterday_closing_price)
diff_percent = (difference / yesterday_closing_price) * 100

print(diff_percent)

if diff_percent > .1:
    news_response = requests.get(url=NEWS_ENDPOINT, params=news_parameters)
    news_response.raise_for_status()
    articles = news_response.json()["articles"][:3]

    formatted_articles = [f"Headline: {article['title']}. \nBrief: {article['description']}" for article in articles]

    print(formatted_articles)
    client = Client(TWILIO_ACCT_ID, TWILIO_AUTH_TOKEN)
    for article in formatted_articles:
        message = client.messages.create(
            body=article,
            from_="+12565677934",
            to="+12525066205"
        )
