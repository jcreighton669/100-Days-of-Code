from twilio.rest import Client

TWILIO_SID = "ACb22d8935c06d47d6a14c27d8ab672c60"
TWILIO_AUTH_TOKEN = "101fe7915666b5055e72a0dc7e1d42b4"
TWILIO_VIRTUAL_NUMBER = "+12565677934"
TWILIO_VERIFIED_NUMBER = "+12525066205"


class NotificationManager:
    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    def send_sms(self, message):
        message = self.client.messages.create(
            body=message,
            from_=TWILIO_VIRTUAL_NUMBER,
            to=TWILIO_VERIFIED_NUMBER,
        )
        print(message.sid)
