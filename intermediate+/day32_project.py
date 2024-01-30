# Automated Birthday Wisher
import os
from dotenv import load_dotenv
import smtplib
import datetime as dt
import pandas
import random


load_dotenv()

my_email = os.getenv('EMAIL_FROM')
password=os.getenv('PASSWORD_FROM')

now = dt.datetime.now()
today_month = now.month
today_day= now.day

today = (today_month, today_day)

data = pandas.read_csv("./birthday_wisher_files/birthdays.csv")

birthdays_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}

if (today_month, today_day) in birthdays_dict:
    birthday_person = birthdays_dict[today]
    letter_random = random.randint(1,3)
    with open(f"./birthday_wisher_files/letter_templates/letter_{letter_random}.txt") as file:
        letter_file = file.read()
        letter_file = letter_file.replace("[NAME]",birthday_person["name"] )


    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email,password=password)
        connection.sendmail(from_addr=my_email, to_addrs=birthday_person["email"], msg=f"Subject:Happy Birthday!!\n\n{letter_file}")
        connection.close()
