import requests

import os
from dotenv import load_dotenv
from flight_deals_files.flight_data import FlightData

load_dotenv()

TEQUILA_ENDPOINT= os.getenv('TEQUILA_ENDPOINT')
TEQUILA_API_KEY= os.getenv('TEQUILA_API_KEY')

headers = {
    "apikey": TEQUILA_API_KEY
}

class FlightSearch:

    def get_code(self, city):
       
        query={
            "term": city,
            "location_types":"city"
        }
        response = requests.get(url=f"{TEQUILA_ENDPOINT}/locations/query", headers=headers, params=query )
        response.raise_for_status()
        code = response.json()["locations"][0]["code"]
        return code
    
    def check_flights(self, origin_city_code, destination_city_code, from_time, to_time):
        query = {
           "fly_from": origin_city_code,
           "fly_to": destination_city_code,
           "date_from": from_time.strftime("%d/%m/%Y"),
           "date_to":to_time.strftime("%d/%m/%Y"),
           "nights_in_dst_from": 7,
           "nights_in_dst_to": 30,
           "flight_type": "round",
           "one_for_city": 1,
           "max_stopovers": 0,
           "curr": "GBP"
        }
        response = requests.get(url=f"{TEQUILA_ENDPOINT}/v2/search", headers=headers, params=query )

        stopovers = 0
        try:
            data=response.json()["data"][0]
        except IndexError:
            stopovers = 1
            has_stopover = True
            while has_stopover:
                query["max_stopovers"] = stopovers 
                response = requests.get(url=f"{TEQUILA_ENDPOINT}/v2/search", headers=headers, params=query )
                try:
                    data=response.json()["data"][0]
                except IndexError:
                    has_stopover = True
                    stopovers += 1
                else:
                    flight_data=FlightData(
                        price = data["price"], 
                        origin_city= data["route"][0]["cityFrom"],   
                        origin_airport= data["route"][0]["flyFrom"], 
                        destination_city= data["route"][0]["cityTo"],  
                        destination_airport= data["route"][0]["flyTo"],   
                        out_date= data["route"][0]["local_departure"].split("T")[0],
                        return_date= data["route"][1]["local_departure"].split("T")[0], 
                        stop_overs=stopovers,
                        via_city=data["route"][0]["cityTo"]
                    )
                    print(f"{flight_data.destination_city}: £{flight_data.price}")
                    has_stopover = False
                    return flight_data
        else:
            flight_data=FlightData(
                price = data["price"], 
                origin_city= data["route"][0]["cityFrom"],   
                origin_airport= data["route"][0]["flyFrom"], 
                destination_city= data["route"][0]["cityTo"],  
                destination_airport= data["route"][0]["flyTo"],   
                out_date= data["route"][0]["local_departure"].split("T")[0], 
                return_date= data["route"][1]["local_departure"].split("T")[0], 
            )
            print(f"{flight_data.destination_city}: £{flight_data.price}")
            return flight_data
    