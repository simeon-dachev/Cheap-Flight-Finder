import smtplib
from tkinter import messagebox
# from flight_data import FlightData


class NotificationManager:
    def __init__(self, flight_data):
        self.def_msg_one_way = None
        self.flight_data = flight_data
        self.def_msg_head = f"Hey!\nThe flight {self.flight_data.city_from} ({self.flight_data.airport_from}) - " \
                            f"{self.flight_data.city_to} ({self.flight_data.airport_to}) is less than {self.flight_data.price_cutoff} BGN - only " \
                            f"{self.flight_data.total_price} BGN. It has {self.flight_data.stopovers} stopovers." \
                            f" There are {self.flight_data.available_seats} " \
                            f"available seats left:\n\n"
        self.def_start_msg = f"Subject:Cheap Flight {self.flight_data.city_from} - " \
                             f"{self.flight_data.city_to}!\n\n"
        self.my_email = "testingangeladay32@gmail.com"
        self.my_pass = "hzmcodiwwegyiyyq"
        # self.return_part_msg = f"{self.flight_data.city_to} - {self.flight_data.city_from}:\n"\
        #                        f"Departure: {self.flight_data.dep_date_d2} at {self.flight_data.dep_time_d2} local time;\n"\
        #                        f"Arrival: {self.flight_data.arr_date_d2} at {self.flight_data.arr_time_d2} local time.\n"\
        #                        f"Airline code: {self.flight_data.airline_code_d2}"
        self.ind_fl_msgs = ""
        self.window_title = "Flight found!"
        self.window_text = ""

    def send_email(self, recipient):
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=self.my_email, password=self.my_pass)

            connection.sendmail(from_addr=self.my_email,
                                to_addrs=recipient,
                                msg=self.default_message())

        print(f"Email for a flight {self.flight_data.city_from} - {self.flight_data.city_to} sent!")

    def show_answer_window(self):
        self.window_text = self.default_message()
        messagebox.showinfo(title=self.window_title, message=self.window_text)

    def default_message(self):
        if self.flight_data.num_flights == 0:
            self.def_msg_one_way = f"Departure: {self.flight_data.dep_date_d1} at {self.flight_data.dep_time_d1} local time;\n" \
                                   f"Arrival: {self.flight_data.arr_date_d1} at {self.flight_data.arr_time_d1} local time.\n" \
                                   f"Airline code: {self.flight_data.airline_code_d1}\n\n"
            return self.def_start_msg + self.def_msg_head + self.def_msg_one_way
        else:
            for ind in range(self.flight_data.num_flights):
                new_msg = f"{self.flight_data.route[ind]['cityFrom']} ({self.flight_data.route[ind]['flyFrom']}) - " \
                          f"{self.flight_data.route[ind]['cityTo']} ({self.flight_data.route[ind]['flyTo']}):\n" \
                          f"Departure: {self.flight_data.dep_dates[ind]} at {self.flight_data.dep_times[ind]} local time;\n" \
                          f"Arrival: {self.flight_data.arr_dates[ind]} at {self.flight_data.arr_times[ind]} local time.\n" \
                          f"Airline code: {self.flight_data.airline_codes[ind]}\n\n"
                # print(new_msg)
                self.ind_fl_msgs += new_msg
            if not self.flight_data.one_way:
                def_start_msg_ret = f"Subject:Cheap Return Flight {self.flight_data.city_from} - " \
                                    f"{self.flight_data.city_to}!\n\n"
                def_head_msg_ret = f"Hey!\nThe return flight {self.flight_data.city_from} ({self.flight_data.airport_from}) - " \
                                   f"{self.flight_data.city_to} ({self.flight_data.airport_to}) is less than {self.flight_data.price_cutoff} BGN - only " \
                                   f"{self.flight_data.total_price} BGN. It has {self.flight_data.stopovers} stopovers. " \
                                   f"There are {self.flight_data.available_seats} " \
                                   f"available seats left:\n\n"
                return def_start_msg_ret + def_head_msg_ret + self.ind_fl_msgs
            else:
                return self.def_start_msg + self.def_msg_head + self.ind_fl_msgs



