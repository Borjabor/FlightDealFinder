import requests
import os

AMADEUS_API_KEY = os.environ.get("AMADEUS_TOKEN")
AMADEUS_API_SECRET = os.environ.get("AMADEUS_SECRET")

class FlightSearch:
    def __init__(self):
        self._api_key = AMADEUS_API_KEY
        self._api_secret = AMADEUS_API_SECRET
        self._token = self.get_oauth_token()
    
    def get_oauth_token(self):
        amadeus_token_request = "https://test.api.amadeus.com/v1/security/oauth2/token"

        header = {
            "Content-Type": "application/x-www-form-urlencoded"
        }

        amadeus_data = {
            "grant_type": "client_credentials",
            "client_id": self._api_key,
            "client_secret": self._api_secret
        }
        
        amadeus_token_response = requests.post(url=amadeus_token_request, headers=header, data=amadeus_data)
        amadeus_token_response.raise_for_status()
        token_data = amadeus_token_response.json()
        token = token_data["access_token"]
               
        return token
    
    def get_destination_code(self, city_name):
        location_request = "https://test.api.amadeus.com/v1/reference-data/locations/cities"

        header = {
            "Authorization": f"Bearer {self._token}"
        }

        amadeus_data = {
            "keyword": city_name,
            "max": "5"
        }

        location_response = requests.get(url=location_request, headers=header, params=amadeus_data)
        location_response.raise_for_status()
        iata_code = location_response.json()["data"][0]["iataCode"]
        
        return iata_code
    
    def get_flight_prices(self, origin_city_code, destination_city_code, depart_date, return_date, max_price):
        search_request = "https://test.api.amadeus.com/v2/shopping/flight-offers"

        header = {
            "Authorization": f"Bearer {self._token}"
        }
        
        #using get requests for return date
        amadeus_data = {
            "originLocationCode": origin_city_code,
            "destinationLocationCode": destination_city_code,
            "departureDate": depart_date.strftime("%Y-%m-%d"),
            "returnDate": return_date.strftime("%Y-%m-%d"),
            "adults": 1,
            "currencyCode": "USD",
            "maxPrice": max_price
        }
    
        
        search_response = requests.get(url=search_request, headers=header, params=amadeus_data)
        
        if search_response.status_code != 200:
            print(f"check_flights() response code: {search_response.status_code}")
            print("There was a problem with the flight search.\n")
            print("Response body:", search_response.text)
            return None

        return search_response.json()