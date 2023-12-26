# rain alert

import requests
from twilio.rest import Client

LAT = -22.289181
LONG = -42.534561

API_KEY = "9d7c65f89dd09a5b7543f5d4f6b54107"
URL = "http://api.openweathermap.org/data/2.5/forecast"

account_sid = 'AC0aefa6bd8bf270e3df43fc635947a0ed'
auth_token = 'a9fa40f6438e5b37db472cb45343a8c6'


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
       from_='+14252766558',
       to='+55229999999999'
    )
   print(message.status)
