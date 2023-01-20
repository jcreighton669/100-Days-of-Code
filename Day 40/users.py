import requests

USER_SHEET_ENDPOINT = "https://api.sheety.co/7d6aad94864a838a7fc7a9b98a0f2345/flightDeals/users"

intro = "Welcome to Angela's Flight Club.\nWe find the best flight deals and email you."

print(intro)
firstName = input("What is your first name?\n")
lastName = input("What is your last name?\n")

email = input("What is your email?\n")
email_confirmation = input("Type your email again.")

if email == email_confirmation:
    requests.post(
        url=USER_SHEET_ENDPOINT,
    )
