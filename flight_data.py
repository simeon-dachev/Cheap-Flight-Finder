# Searching only return flights

class FlightData:
    def __init__(self, data: list, price_cutoff: int):
        self.data = data
        self.route = self.data[0]["route"]
        self.num_flights = len(self.route)
        self.city_from = self.data[0]["cityFrom"]
        self.airport_from = self.data[0]["flyFrom"]
        self.city_to = self.data[0]["cityTo"]
        self.airport_to = self.data[0]["flyTo"]
        self.total_price = self.data[0]["price"]
        self.available_seats = self.data[0]["availability"]["seats"]
        # self.flights_found_already = []
        if self.available_seats is None:
            self.available_seats = "many"
        self.price_cutoff = price_cutoff
        if self.data[0]["duration"]["return"] == 0:
            self.one_way = True
            self.stopovers = self.num_flights - 1
        else:
            self.one_way = False
            self.stopovers = self.num_flights - 2

        self.dep_dates = []
        self.dep_times = []
        self.arr_dates = []
        self.arr_times = []
        self.airline_codes = []

        for ind in range(self.num_flights):
            self.dep_dates.append(self.route[ind]["local_departure"][:10])
            self.dep_times.append(self.route[ind]["local_departure"][11:16])
            self.arr_dates.append(self.route[ind]["local_arrival"][:10])
            self.arr_times.append(self.route[ind]["local_arrival"][11:16])
            self.airline_codes.append(self.route[0]["airline"])

        print(self.dep_dates, self.arr_dates)
    # def write_flight_id_in_file(self):
    #     for item in self.route:
    #         try:
    #             with open("flights_already_found.txt", mode="a") as flights_file:
    #                 flights_file.write(item["flight_no"])
    #                 flights_file.write("\n")
    #         except FileNotFoundError:
    #             with open("flights_already_found.txt", mode="w") as flights_file:
    #                 flights_file.write(item["flight_no"])
    #
    # def read_flight_id_in_file(self):
    #     try:
    #         with open("flights_already_found.txt", mode="r") as flights_file:
    #             lines = flights_file.readlines()
    #             for line in lines:
    #                 line.strip()
    #             print(lines)
    #     except FileNotFoundError:
    #         print("No flights found until now")
    #         pass




        # self.dep_date_d1 = self.route[0]["local_departure"][:10]
        # self.dep_time_d1 = self.route[0]["local_departure"][11:16]
        # self.arr_date_d1 = self.route[0]["local_arrival"][:10]
        # self.arr_time_d1 = self.route[0]["local_arrival"][11:16]
        # self.airline_code_d1 = self.route[0]["airline"]
        # if self.data[0]["duration"]["return"] == 0:
        #     self.one_way = True
        # else:
        #     self.one_way = False
        #
        # if not self.one_way:
        #     self.dep_date_d2 = self.route[1]["local_departure"][:10]
        #     self.dep_time_d2 = self.route[1]["local_departure"][11:16]
        #     self.arr_date_d2 = self.route[1]["local_arrival"][:10]
        #     self.arr_time_d2 = self.route[1]["local_arrival"][11:16]
        #     self.airline_code_d2 = self.route[1]["airline"]

    def deal_present(self):
        '''Returns True if a return flight cheaper than or equal to the price cutoff is found.
        Otherwise returns False.'''
        if self.total_price <= self.price_cutoff:
            return True
        return False

