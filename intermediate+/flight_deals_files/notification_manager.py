import os
from dotenv import load_dotenv
from twilio.rest import Client
import smtplib

load_dotenv()

account_sid = os.getenv('ACCOUNT_SID')
auth_token = os.getenv('AUTH_TOKEN')

sms_from = os.getenv('SMS_FROM')
sms_to = os.getenv('SMS_TO')

my_email = os.getenv('EMAIL_FROM')
password=os.getenv('PASSWORD_FROM')



class NotificationManager:
    def __init__(self):
        self.client = Client(account_sid, auth_token)

    def send_sms(self, message):
        message = self.client.messages.create(
            body=message,
            from_=sms_from,
            to=sms_to
            )
        print(message.sid)

    def send_emails(self, emails, message):
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=my_email,password=password)
            for email in emails:
                connection.sendmail(from_addr=my_email, to_addrs=email, msg=f"Subject:New Low Price Flight!\n\n{message}".encode('utf-8'))
        connection.close()
