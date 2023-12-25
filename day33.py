#day 33
#API'S

import requests
import smtplib
from datetime import datetime
import time

my_email = "teste@gmail.com"
password="gjlztlmeifwusepf"

LAT = -22.289181
LONG = -42.534561


response = requests.get(url = "http://api.open-notify.org/iss-now.json")
response.raise_for_status()

data = response.json()
longitude = float(data["iss_position"]["longitude"])
latitude = float(data["iss_position"]["latitude"])

parametres = {
    "lat":LAT,
    "lng":LONG,
    "formatted": 0
}
response = requests.get("https://api.sunrise-sunset.org/json", params=parametres)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

time_now = datetime.now()
time_hour = time_now.hour


is_dark =  sunrise >= time_hour >= sunset
current_location_lng = LONG - 5 <= longitude <= LONG + 5
current_location_lat = LAT - 5 <= latitude <= LAT + 5


while True:
    time.sleep(20)
    if(is_dark and current_location_lng and current_location_lat):
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=my_email,password=password)
            connection.sendmail(from_addr=my_email, to_addrs="bruna@gmail.com", msg=f"Subject:ISS Notifier\n\n Look to the sky")
            connection.close()

     

 