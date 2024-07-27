import requests
import os

SHEETY_PRICES_ENDPOINT = os.environ.get("SHEETY_PRICES_ENDPOINT")
SHEETY_USERS_ENDPOINT = os.environ.get("SHEETY_USERS_ENDPOINT")
SHEETY_TOKEN = os.environ.get("SHEETY_TOKEN")

class DataManager:
    def __init__(self):
        self.price_sheet_endpoint = SHEETY_PRICES_ENDPOINT
        self.user_sheet_endpoint = SHEETY_USERS_ENDPOINT
        self.header = {
            "Authorization": f"Bearer {SHEETY_TOKEN}"
        }
    
    def get_destination_data(self):
        self._response = requests.get(url=self.price_sheet_endpoint, headers=self.header)
        self._destination_data = self._response.json()

        return self._destination_data
      
    def update_sheet_data(self, data, row):
        self._response = requests.put(url=f"{self.price_sheet_endpoint}/{row}", json=data, headers=self.header)
        
    def get_user_emails(self):
        self._response = requests.get(url=self.user_sheet_endpoint, headers=self.header)
        self._user_emails = self._response.json()["users"]

        return self._user_emails