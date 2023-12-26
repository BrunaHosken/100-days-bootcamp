# rain alert

import requests
import os
from twilio.rest import Client
from dotenv import load_dotenv

load_dotenv()

LAT = -22.289181
LONG = -42.534561

API_KEY = os.getenv('API_KEY')
URL = "http://api.openweathermap.org/data/2.5/forecast"

account_sid = os.getenv('ACCOUNT_SID')
auth_token = os.getenv('AUTH_TOKEN')

sms_from = os.getenv('SMS_FROM')
sms_to = os.getenv('SMS_TO')
print(API_KEY)



parametres = {
    "lat":LAT,
    "lon":LONG,
    "appid": API_KEY,
    "cnt": 4
}

response = requests.get(URL,params = parametres)
response.raise_for_status()

list_weather = response.json()

will_rain = False
for data in list_weather["list"]:
    weather = data["weather"]
    for index in weather:
        if(index["id"]<= 700):
            will_rain = True

if will_rain:
   client = Client(account_sid, auth_token)
   message = client.messages.create(
       body="It's rain today. Remember to bring an umbrella!!",
       from_=sms_from,
       to=sms_to
    )
   print(message.status)
