#day 33
#API'S

import requests
import smtplib
from datetime import datetime
import time

my_email = "teste@gmail.com"
password="gjlztlmeifwusepf"

MY_LAT = -22.289181
MY_LONG = -42.534561

def iss_position():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    latitude = iss_latitude >= MY_LONG-5 and iss_latitude <= MY_LONG+5
    longitude = iss_longitude >= MY_LONG-5 and iss_longitude <= MY_LAT+5

    return latitude and longitude

def is_dark():
    parametres = {
        "lat":MY_LAT,
        "lng":MY_LONG,
        "formatted": 0
    }
    response = requests.get("https://api.sunrise-sunset.org/json", params=parametres)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now()
    time_hour = time_now.hour

    return time_hour >= sunset or time_hour <= sunrise

while True:
    time.sleep(30)
    if( iss_position() and is_dark()):
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=my_email,password=password)
            connection.sendmail(from_addr=my_email, to_addrs="bruna@gmail.com", msg=f"Subject:ISS Notifier\n\n Look to the sky")
            connection.close()
     

 