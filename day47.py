import requests
import os
from dotenv import load_dotenv
from bs4 import BeautifulSoup
import smtplib

load_dotenv()

USER_AGENT =  os.getenv('USER_AGENT')
my_email = os.getenv('EMAIL_FROM')
password=os.getenv('PASSWORD_FROM')
to_email = os.getenv('EMAIL_TO')
TARGET_PRICE = 100

url = "https://www.amazon.com/dp/B075CYMYK6?psc=1&ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6"

headers={
    "User-Agent":USER_AGENT,
    "Accept-Language": "en-US,en;q=0.5",
    "sec-ch-ua-platform": "Linux",
    "Accept-Encoding": "gzip, deflate, br"
}
response = requests.get(url=url, headers=headers)

soup = BeautifulSoup(response.content, "lxml")

price = soup.find(class_="a-offscreen").getText()
floatPrice = float(price.split("$")[1])
product = soup.find(id="productTitle").getText().strip()

if(floatPrice < TARGET_PRICE):
   message = f"{product} is now {price}!\n\n Check the website: {url}"
   with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email,password=password)
        connection.sendmail(from_addr=my_email, to_addrs=to_email, msg=f"Subject:Amazon Price Alert!\n\n {message}".encode("utf-8"))
        connection.close()
     