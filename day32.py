#day 32
#Send Email SMTP

# Gmail: smtp.gmail.com
# Hotmail: smtp.live.com
# Outlook: outlook.office365.com
# Yahoo: smtp.mail.yahoo.com
# smtplib.SMTP("smtp.gmail.com", port=587)


import smtplib
import datetime as dt
import random


my_email = "teste@gmail.com"
password="gjlztlmeifwusepf"

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
        connection.sendmail(from_addr=my_email, to_addrs="bruna@gmail.com", msg=f"Subject:Motivational Quote\n\n{chosen_quote}")
        connection.close()



# date_of_birth = dt.datetime(year=1997, month=3, day=12)


