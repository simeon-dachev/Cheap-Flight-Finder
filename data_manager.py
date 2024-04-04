import requests
import os
from flight_search import FlightSearch
flight_search = FlightSearch("Milan")

class DataManager:
    def __init__(self):
        self.endpoint = "https://api.sheety.co/2b9d15df96e097fb5d05670b373139df/flightDealFinder/prices"
        self.cities = []
        self.airport_codes = []
        self.cutoffs = []
        self.auth = os.environ["AUTH"]
        self.auth = "Bearer CeckaMentiSheety"
        self.header = {
            "Authorization": self.auth
        }
        self.get_all_rows()

    def get_all_rows(self):
        ind = 2
        get_response = requests.get(url=f"{self.endpoint}/{ind}", headers=self.header)
        # print(get_response.json())
        while get_response.status_code != 404:
            self.cities.append(get_response.json()["price"]["city"])
            self.airport_codes.append(get_response.json()["price"]["iataCode"])
            self.cutoffs.append(get_response.json()["price"]["lowestPrice"])
            ind += 1
            get_response = requests.get(url=f"{self.endpoint}/{ind}", headers=self.header)

    def get_row(self, ind):
        get_response = requests.get(url=f"{self.endpoint}/{ind}", headers=self.header)
        row = []
        row.append(get_response.json()["price"]["city"])
        row.airport_codes.append(get_response.json()["price"]["iataCode"])
        row.cutoffs.append(get_response.json()["price"]["lowestPrice"])
        return row

    def add_row(self, city: str, cutoff: int):
        airport_code = flight_search.get_city_code(city)
        new_city_info = {
            "price": {
                "city": city,
                "iataCode": airport_code,
                # "iataCode": airport_code,
                "lowestPrice": cutoff,
            }
        }
        response = requests.post(url=self.endpoint, json=new_city_info, headers=self.header)
        response.raise_for_status()
        if response.status_code == 200:
            print(f"{city} added successfully!")
        self.cities.append(city)
        self.airport_codes.append(airport_code)
        self.cutoffs.append(cutoff)

    def update_row(self, row: int, city: str, cutoff: int):
        airport_code = flight_search.get_city_code(city)
        updated_city_info = {
            "price": {
                "city": city,
                "iataCode": airport_code,
                "lowestPrice": cutoff,
            }
        }
        upd_response = requests.put(url=f"{self.endpoint}/{row}", json=updated_city_info, headers=self.header)
        upd_response.raise_for_status()
        if upd_response.status_code == 200:
            print(f"{city} at row {row} updated successfully!")
        self.cities[row - 2] = city
        self.airport_codes[row - 2] = airport_code
        self.cutoffs[row - 2] = cutoff

    def delete_row(self, row: int):
        del_response = requests.delete(url=f"{self.endpoint}/{row}", headers=self.header)
        del_response.raise_for_status()
        if del_response.status_code == 200:
            print(f"Row deleted successfully!")
        del self.cities[row - 2]
        del self.airport_codes[row - 2]
        del self.cutoffs[row - 2]

    def clear_all(self):
        self.cities.clear()
        self.airport_codes.clear()
        self.cutoffs.clear()
        get_response = requests.get(url=f"{self.endpoint}/2", headers=self.header)
        while get_response.status_code != 404:
            requests.delete(url=f"{self.endpoint}/2", headers=self.header)
            get_response = requests.get(url=f"{self.endpoint}/2", headers=self.header)
        print("Table cleared successfully!")


# data_manager = DataManager()
# print(data_manager.cities)
# data_manager.clear_all()
# data_manager.add_row("Milan", "BGY", 20)
# data_manager.add_row("Seville", "SVQ", 45)
# data_manager.update_row(2, "Milan", "BGY", 20)
# get_response = requests.get(url=f"{data_manager.endpoint}/7", headers=data_manager.header)
# print(get_response.json())
# print(data_manager.cities)
