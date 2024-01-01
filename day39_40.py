# day 39 and 40
#Flight Deals

from flight_deals_files.data_manager import DataManager
from flight_deals_files.flight_search import FlightSearch
from datetime import datetime, timedelta
from flight_deals_files.notification_manager import NotificationManager

data_manager = DataManager()
flight_search = FlightSearch()
notification_manager = NotificationManager()

sheet_data = data_manager.get_destination()
ORIGIN_CITY_IATA = "LON"

if sheet_data[0]["iataCode"] == "":
    for data in sheet_data:
        data["iataCode"] = flight_search.get_code(data["city"])
    data_manager.sheet_data = sheet_data
    data_manager.update_destination()

tomorrow = datetime.now() + timedelta(days=1)
six_month = datetime.now() + timedelta(days=6*30)

    
for destination in sheet_data:
    flight = flight_search.check_flights(
        ORIGIN_CITY_IATA,
        destination["iataCode"],
        from_time = tomorrow,
        to_time = six_month
    )
    
    if flight is None:
        continue

    if(flight.price < destination["lowestPrice"]):
        users = data_manager.get_users()
        emails = [row["email"] for row in users]

        message = f"Low price alert! Only £{flight.price} to fly from {flight.origin_city}-{flight.origin_airport} to {flight.destination_city}-{flight.destination_airport}, from {flight.out_date} to {flight.return_date}."
        
        if flight.stop_overs > 0:
            message += f"\nFlight has {flight.stop_overs} stop over, via {flight.via_city}."
        print(message)    
        notification_manager.send_sms(message)
        notification_manager.send_emails(emails, message)
