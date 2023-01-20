import smtplib

from twilio.rest import Client

TWILIO_SID = "ACb22d8935c06d47d6a14c27d8ab672c60"
TWILIO_AUTH_TOKEN = "a67466e809901d79e41d7adb9df9f316"
TWILIO_VIRTUAL_NUMBER = "+12565677934"
PHONE_NUMBER = "+12525066205"
MAIL_PROVIDER_SMTP_ADDRESS = "smtp.gmail.com"
MY_EMAIL = "justincreighton2006@gmail.com"
MY_PASSWORD = "iblhtmnhdvhhzqaj"

class NotificationManager:
    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    def send_sms(self, message):
        message = self.client.messages.create(
            body=message,
            from_=TWILIO_VIRTUAL_NUMBER,
            to=PHONE_NUMBER
        )
        print(message.sid)

    def send_emails(self, emails, message, google_flight_link):
        with smtplib.SMTP(MAIL_PROVIDER_SMTP_ADDRESS) as connection:
            connection.starttls()
            connection.login(MY_EMAIL, MY_PASSWORD)
            for email in emails:
                connection.sendmail(
                    from_addr=MY_EMAIL,
                    to_addrs=email,
                    msg=f"Subject:New Low Price Flight!\n\n{message}\n{google_flight_link}".encode('utf-8')
                )