#day 32
#Send Email SMTP

# Gmail: smtp.gmail.com
# Hotmail: smtp.live.com
# Outlook: outlook.office365.com
# Yahoo: smtp.mail.yahoo.com
# smtplib.SMTP("smtp.gmail.com", port=587)

import os
from dotenv import load_dotenv
import smtplib
import datetime as dt
import random

load_dotenv()

my_email = os.getenv('EMAIL_FROM')
password=os.getenv('PASSWORD_FROM')

to_email = os.getenv('EMAIL_TO')

now = dt.datetime.now()
# year = now.year
# month= now.month
day_of_weak = now.weekday()

if(day_of_weak == 1):
    with open("./motivational_quotes_files/quotes.txt") as file:
        quotes = file.readlines()
        chosen_quote=random.choice(quotes)

    
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email,password=password)
        connection.sendmail(from_addr=my_email, to_addrs=to_email, msg=f"Subject:Motivational Quote\n\n{chosen_quote}")
        connection.close()



# date_of_birth = dt.datetime(year=1997, month=3, day=12)


