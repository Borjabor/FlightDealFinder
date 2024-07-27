from flight_search import FlightSearch
from flight_data import find_cheapest_flight
from data_manager import DataManager
from notification_manager import NotificationManager
from datetime import datetime, timedelta

flight_search = FlightSearch()
data_manager = DataManager()
notification_manager = NotificationManager()

sheet_data = data_manager.get_destination_data()
origin_city_code = "IATACodeForYourOriginCity" #Replace with your IATA Code, for example, NYC if your origin city is New York
max_connections = 2 #Set your max number of connections; I chose two for personal preference

# Update IATA Codes if any are missing
for i in sheet_data["prices"]:
    if i["iataCode"] == "":
        iata_code = {"price": {"iataCode": flight_search.get_destination_code(i["city"])}}

        data_manager.update_sheet_data(iata_code, i["id"])
    
# Set dates to depart in a month and travel for 2 weeks    
today = datetime.now()
four_weeks_from_today = (today + timedelta(days=28))
six_weeks_from_today = (today + timedelta(days=42))

user_emails = [i["pleaseProvideYourEmail:"] for i in data_manager.get_user_emails()]
        
for destination in sheet_data["prices"]:
    options = []
    #search for flights within a 7 day range
    for i in range(7):
        depart_date = (four_weeks_from_today + timedelta(days=i))
        flights = flight_search.get_flight_prices(
            origin_city_code, 
            destination["iataCode"], 
            depart_date, 
            six_weeks_from_today,
            destination["lowestPrice"]
        )
    
        cheapest_flight = find_cheapest_flight(flights)
        options.append(cheapest_flight)


    cheapest_flight = min(options, key=lambda x: x.price)
    
#Uncomment below to send a notification via WhatsApp

    # notification_manager.send_whatsapp_message(
    #         message_body=f"Low price alert! Only US${cheapest_flight.price} to fly "
    #                      f"from {cheapest_flight.origin_airport} to {cheapest_flight.destination_airport} with {cheapest_flight.stops} stops. "
    #                      f"Leaving {cheapest_flight.out_date} and returning {cheapest_flight.return_date}."
    #     )

#Uncomment below to send a notification via email to every user in an email spreadsheet

    notification_manager.send_email(user_emails, f"Low price alert! Only US${cheapest_flight.price} to fly from {cheapest_flight.origin_airport} to {cheapest_flight.destination_airport} with {cheapest_flight.stops} stops. Leaving {cheapest_flight.out_date} and returning {cheapest_flight.return_date}.")