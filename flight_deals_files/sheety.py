import os
from dotenv import load_dotenv
import requests

load_dotenv()

SHEET_ENDPOINT_USERS= os.getenv('SHEET_ENDPOINT_USERS')
SHEET_API_FLIGHT= os.getenv('SHEET_API_FLIGHT')

headers = {
    "Authorization": SHEET_API_FLIGHT
}

def post_user(first_name, last_name, email):
    body= {
        "user":{
            "firstName":first_name,
            "lastName":last_name,
            "email":email
        }
    }

    response = requests.post(url=SHEET_ENDPOINT_USERS, headers=headers, json=body)
    response.raise_for_status()
    print(response.text)