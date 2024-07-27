import smtplib
import os
from twilio.rest import Client

TWILIO_SID = os.environ.get("TWILIO_SID")
TWILIO_AUTH = os.environ.get("TWILIO_AUTH")
EMAIL = os.environ.get("MY_EMAIL")
PASSWORD = os.environ.get("MY_PASSWORD")
TWILIO_NUMBER = os.environ.get("TWILIO_VIRTUAL_NUMBER")
MY_NUMBER = os.environ.get("MY_NUMBER")

class NotificationManager():
    def __init__(self):
        self._client = Client(TWILIO_SID, TWILIO_AUTH)
        self._email = EMAIL
        self._password = PASSWORD
        
    def send_sms(self, message):
        self._client.messages.create(
            from_= TWILIO_NUMBER,
            body = message,
            to = MY_NUMBER
        )
        
    def send_whatsapp_message(self, message):    
                
        whatsapp_message = self._client.messages.create(
            from_= f"whatsapp:{TWILIO_NUMBER}",
            body = message,
            to = f"whatsapp:{MY_NUMBER}"
        )
        
    def send_email(self, emails, message):
        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(user=self._email, password=self._password)
            for email in emails:
                connection.sendmail(
                    from_addr=self._email,
                    to_addrs=email,
                    msg=f"Subject:Flight Club Low Price Alert!\n\n{message}".encode('utf-8')
                )