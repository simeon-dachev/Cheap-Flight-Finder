import pandas
from flight_search import FlightSearch
flight_search = FlightSearch("Milan")

class Pandas_Data:
    def __init__(self):
        try:
            self.table = pandas.read_csv("pandas_flight_data.csv")
        except FileNotFoundError:
            self.another_one = "yes"
            self.new_city = ""
            self.new_cutoff = ""
            self.new_iata_code = ""
            self.iata_codes = []
            self.cities = []
            self.cutoffs = []
            while self.another_one == "yes":
                self.add_row()
            self.data_dict = {
                "Cities": self.cities,
                "IATA codes": self.iata_codes,
                "Cutoffs": self.cutoffs,
                # "Cities": ["Paris", "Barcelona", "New York"]
                # "Cutoffs": []
            }
            self.data = pandas.DataFrame(self.data_dict)
            self.update_table()
        else:
            self.data = pandas.read_csv("pandas_flight_data.csv")
        finally:
            self.cities = self.table["Cities"].to_list()
            # print(type(self.cities))
            self.iata_codes = self.table["IATA codes"].to_list()
            # print(self.iata_codes)
            self.cutoffs = self.table["Cutoffs"].to_list()

    def add_row(self, city=None, cutoff=None):
        if city is None:
            self.new_city = input("City you want to add: ")
        if cutoff is None:
            self.new_cutoff = input("Max price (BGN) for a return flight to that city: ")
        if city is not None and cutoff is not None:
            self.new_city = city
            self.new_cutoff = cutoff
        self.cities.append(self.new_city)
        self.new_iata_code = flight_search.get_city_code(self.new_city)
        self.iata_codes.append(self.new_iata_code)
        self.cutoffs.append(self.new_cutoff)
        if city is None or cutoff is None:
            print(f"{self.new_city} added successfully!")
            self.another_one = (input("Do you want to add another city? ")).lower()
            while self.another_one != "yes" and self.another_one != "no":
                self.another_one = input('Please type "Yes" or "No": ')
        else:
            self.data.loc[len(self.cities) - 1] = [self.new_city, self.new_iata_code, self.new_cutoff]
            self.update_table()
            print(f"{self.new_city} added successfully!")

    def update_row(self, ind, city, cutoff):
        self.data.at[ind - 1, "Cities"] = city
        iata_code = flight_search.get_city_code(city)
        self.data.at[ind - 1, "Iata codes"] = iata_code
        self.data.at[ind - 1, "Cutoffs"] = cutoff
        print(f"{city} at row {ind} updated successfully!")
        self.data.to_csv("pandas_flight_data.csv", index=False)
        self.table = pandas.read_csv("pandas_flight_data.csv")

    def delete_row(self, ind):
        self.data = self.data.drop(ind)
        print(f"Row {ind} deleted successfully!")

    def update_table(self):
        self.data.to_csv("pandas_flight_data.csv", index=False)
        self.table = pandas.read_csv("pandas_flight_data.csv")

    def print_table(self):
        print(self.table)


# hihi = Pandas_Data()
# hihi.add_row("Barcelona", )
# hihi.print_table()
# data = pandas.read_csv("pandas_flight_data.csv")
# print(data["Cities"].to_list())
# print(hihi.cities)

