import requests
from pprint import pprint

class DataManager:

    def __init__(self):
        # Credentials for basic authentication
        self._user = "secret"
        self._password = "secret"
        self.destination_data = {}
        self.auth = (self._user, self._password)
        self.endpoint = "https://api.sheety.co/05bf06b34dbdf3c951f9c99a26cb3241/flights/prices"

    def get_destination_data(self):
        # Use the Sheety API to GET all the data in the sheet
        response = requests.get(url=self.endpoint, auth=self.auth)
        response.raise_for_status()  # To ensure any HTTP errors are caught
        data = response.json()
        self.destination_data = data["prices"]
        pprint(self.destination_data)  # Pretty print the data
        return self.destination_data

    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                url=f"{self.endpoint}/{city['id']}",
                json=new_data,
                auth=self.auth
            )

            print(response.text)
