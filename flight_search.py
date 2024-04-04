import os
import requests


class FlightSearch:
    def __init__(self, origin_city: str):
        self.endpoint = "https://api.tequila.kiwi.com"
        # self.api_key = os.environ["FLIGHTS_API_KEY"]  # uncomment to run with env variables
        self.api_key = "ayueA5mqgQ2emMJtQxfIWSwV-Yg_DcGK"
        self.header = {
            "apikey": self.api_key
        }
        self.from_city = origin_city

    def get_city_code(self, city: str):
        locations_data = {
            "term": city,
            "locale": "en-US",
            "location_types": "airport",
            "limit": 1,
            "active_only": True,
            "sort": "name"
        }
        response = requests.get(url=f"{self.endpoint}/locations/query", params=locations_data, headers=self.header)
        # print(response.json())
        return response.json()["locations"][0]["city"]["code"]

    def search_query(self, destination_city: str,
                     date_from: str, date_to: str, max_stopovers: int,
                     date_from_ret=None, date_to_ret=None):
                     # min_nights_stay=None, max_nights_stay=None):
        self.dest = destination_city
        if date_from_ret is not None and date_to_ret is not None:
        # if min_nights_stay is not None and max_nights_stay is not None:
            print("Searching for a return flight...")
            search_data = {
                "fly_from": self.get_city_code(self.from_city),
                "fly_to": self.get_city_code(destination_city),
                "date_from": date_from,
                "date_to": date_to,
                "return_from": date_from_ret,
                "return_to": date_to_ret,
                # "nights_in_dst_from": min_nights_stay,
                # "nights_in_dst_to": max_nights_stay,
                "adults": 1,
                "children": 0,
                "selected_cabins": "M",  # Search economy class by default
                # "flight_type": "round",
                "curr": "BGN",
                "price_from": 0,
                "price_to": 1000000,
                "max_stopovers": max_stopovers,
                "sort": "price",
                # "sort": "quality",
                "limit": 1
            }
        else:
            print("Searching for a one-way flight...")
            search_data = {
                "fly_from": self.get_city_code(self.from_city),
                "fly_to": self.get_city_code(destination_city),
                "date_from": date_from,
                "date_to": date_to,
                # "nights_in_dst_from": min_nights_stay,
                # "nights_in_dst_to": max_nights_stay,
                "ret_from_diff_city": False,
                "ret_to_diff_city": False,
                "adults": 1,
                "children": 0,
                "selected_cabins": "M",  # Search economy class by default
                # "flight_type": "round",
                "curr": "BGN",
                "price_from": 0,
                "price_to": 1000000,
                "max_stopovers": max_stopovers,
                "sort": "price",
                # "sort": "quality",
                "limit": 1
            }
        # print(search_data)
        response = requests.get(url=f"{self.endpoint}/v2/search", params=search_data, headers=self.header)
        # print(response.json())
        all_flights_data = response.json()["data"]
        # print(all_flights_data)
        # print(all_flights_data)
        # print(all_flights_data)
        # for flight in all_flights_data:
        #     print(f"\nDeparts: {flight['local_departure']}")
        #     print(f"Arrives: {flight['local_arrival']}")
        #     print(f'Price: {flight["price"]}, Airline: {flight["airlines"]}')
        return all_flights_data


# flight_searcher = FlightSearch("Milan")
# print(flight_searcher.get_city_code("Vienna"))
# data_ = flight_searcher.search_query("Vienna", "25/09/2023", "16/11/2023", 10, 2, 6)
# print(data_)
