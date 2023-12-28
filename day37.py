#day 37
#habit tracking (pixela)

import requests
import os
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()

pixela_endpoint = "https://pixe.la/v1/users"
PIXELA_API_TOKEN = os.getenv('PIXELA_API_KEY')
PIXELA_USERNAME = os.getenv('PIXELA_USERNAME')

graph_endpoint= f"{pixela_endpoint}/{PIXELA_USERNAME}/graphs"



user_params = {
    "token": PIXELA_API_TOKEN,
    "username": PIXELA_USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor":"yes"
}

graph_params ={
    "id":"graph1",
    "name":"Webtoon Graph",
    "unit":"chapter",
    "type":"int",
    "color":"kuro"
}

pixel_endpoint=f"{pixela_endpoint}/{PIXELA_USERNAME}/graphs/{graph_params['id']}"

today = datetime.now().strftime("%Y%m%d")

headers = {
    "X-USER-TOKEN": PIXELA_API_TOKEN
}

pixel_params = {
    "date": today,
    "quantity": "7"
}

graph_update_params = {
    "color": "shibafu"
}

pixel_update_params = {
    "quantity": "27"
}

pixel_endpoint_update=f"{pixela_endpoint}/{PIXELA_USERNAME}/graphs/{graph_params['id']}/{today}"

pixel_endpoint_delete=f"{pixela_endpoint}/{PIXELA_USERNAME}/graphs/{graph_params['id']}/{today}"

# response = requests.post(url=pixela_endpoint, json=user_params)
# response = requests.post(url=graph_endpoint, json=graph_params, headers= headers)
response = requests.post(url=pixel_endpoint, json=pixel_params, headers= headers)
# response = requests.put(url=pixel_endpoint, json=graph_update_params, headers= headers)
# response = requests.put(url=pixel_endpoint_update, json=pixel_update_params, headers= headers)
# response = requests.delete(url=pixel_endpoint_delete, headers= headers)
response.raise_for_status()
print(response.text)

