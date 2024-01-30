#day 36
#stock trading new alert

import requests
import os
from twilio.rest import Client
from dotenv import load_dotenv

load_dotenv()

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

news_api_key = os.getenv('NEWS_API_KEY')
stock_api_key = os.getenv('STOCK_API_KEY')

account_sid = os.getenv('ACCOUNT_SID')
auth_token = os.getenv('AUTH_TOKEN')

sms_from = os.getenv('SMS_FROM')
sms_to = os.getenv('SMS_TO')

messages = []

def get_news():
    global messages
    parametres = {
    "q":COMPANY_NAME,
    "apiKey":news_api_key,
    "sortBy": "relevancy"
    }

    response = requests.get(NEWS_ENDPOINT,params = parametres)
    response.raise_for_status()

    data = response.json()
    news = data["articles"][:3]
    messages = [f"{STOCK_NAME}: {symbol} {percentage}%\n Headline: {article['title']} \nBrief: {article['description']}" for article in news]


def send_message():
    client = Client(account_sid, auth_token)
    for sms in messages:
        message = client.messages.create(
        body=sms,
        from_=sms_from,
        to=sms_to
        )
        print(message.status)

parametres = {
    "function":"TIME_SERIES_DAILY",
    "symbol":STOCK_NAME,
    "apikey": "stock_api_key"
}

response = requests.get(STOCK_ENDPOINT,params = parametres)
response.raise_for_status()

data = response.json()['Time Series (Daily)']
days_list = list(data.items())
last_two_days= days_list[:2]
yesterday_closing_price = float(last_two_days[0][1]["4. close"])
previous_yesterday_closing_price = float(last_two_days[1][1]["4. close"])

dif = abs(yesterday_closing_price - previous_yesterday_closing_price)
percentage =round( (yesterday_closing_price / previous_yesterday_closing_price)*100 -100, 2)
print(percentage)

if dif > 0:
    symbol = "🔺"
elif dif < 0:
    symbol = "🔻"
else:
    symbol = "📊"

if percentage>=5 or percentage<= -5:
    get_news()
    send_message()


