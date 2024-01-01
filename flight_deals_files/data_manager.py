import requests

import os
from dotenv import load_dotenv

load_dotenv()

SHEET_ENDPOINT_USERS= os.getenv('SHEET_ENDPOINT_USERS')
SHEET_ENDPOINT_FLIGHT= os.getenv('SHEET_ENDPOINT_FLIGHT')
SHEET_API_FLIGHT= os.getenv('SHEET_API_FLIGHT')

headers = {
    "Authorization": SHEET_API_FLIGHT
}

class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.sheet_data = {}

    def get_destination(self):
        
        response = requests.get(SHEET_ENDPOINT_FLIGHT, headers=headers)
        response.raise_for_status()
        data = response.json()
        self.sheet_data =  data["prices"]
        return self.sheet_data
    
    def update_destination(self):
         for city in self.sheet_data:
           new_data = {
               "price":{
                   "iataCode":city["iataCode"]
               }
           }
           response = requests.put(url=f"{SHEET_ENDPOINT_FLIGHT}/{city['id']}", json=new_data, headers=headers)
           print(response.text)

    def get_users(self):
        response = requests.get(SHEET_ENDPOINT_USERS, headers=headers)
        response.raise_for_status()
        data = response.json()
        self.sheet_data =  data["users"]
        return self.sheet_data