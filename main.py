from flight_search import FlightSearch
from datetime import datetime, timedelta
from data_manager import DataManager
# from csv_data_manager import Pandas_Data
from flight_data import FlightData
from notification_manager import NotificationManager
# from ui import UI
from tkinter import *
from tkinter import messagebox

# VERSION 1: WITHOUT GUI AND USING GOOGLE SHEETS:

# data_manager = DataManager()
# new_flight_search = FlightSearch("Milan")
#
# # data_manager.update_row(3, "Madrid", 80)
# # data_manager.update_row(4, "Seville", 100)
# # data_manager.update_row(5, "Naples", 50)
# # data_manager.update_row(7, "Reykjavik", 100)
# # data_manager.add_row("Sofia", 30)
# # data_manager.add_row("Eindhoven", 100)
# # data_manager.add_row("Palermo", 50)
# # data_manager.add_row("Catania", 50)
# # data_manager.add_row("Vienna", 80)
# # data_manager.add_row("Madeira", 100)
# # data_manager.add_row("Porto", 50)
# # data_manager.add_row("Bratislava", 50)
# # data_manager.delete_row(8)
# # data_manager.clear_all()
#
# date_now = datetime.now().date()
# # Searching for a return flight in 1-3 months time:
# departure_date_start = (date_now + timedelta(days=30)).strftime("%d/%m/%Y")
# departure_date_end = (date_now + timedelta(days=90)).strftime("%d/%m/%Y")
# # By default: Search for min 2 and max 6 nights spent
# nights_spent_min = 2
# nights_spent_max = 6
# recipient = "pumpalmanatarka@gmail.com"
# # departure_date_start = input("Please enter a departure date in this format: DD/MM/YYYY: ")
# # departure_date_end = input("Please enter an arrival date in this format: DD/MM/YYYY: ")
# # recipient = input("Please enter your email: ")
#
# for city in data_manager.cities:
#     # budget = data_manager.cutoffs[data_manager.cities.index(city)]
#     data_for_flight_data = new_flight_search.search_query(city, departure_date_start, departure_date_end, 10,
#                                                           nights_spent_min, nights_spent_max)
#     price_cutoff = data_manager.cutoffs[data_manager.cities.index(city)]
#     flight_data = FlightData(data_for_flight_data, price_cutoff)
#
#     if flight_data.deal_present():
#         notif_manager = NotificationManager(flight_data)
#         notif_manager.send_email(recipient)
#
#     else:
#         print(f"No cheap flights to {city} found around the selected dates.")


# ##################################################################################
# VERSION 2: WITH GUI AND NOT USING GOOGLE SHEETS:
# (NOTE: For this version, uncomment also lines 32, 35, 43, 44, 64, 65
# and comment lines 33, 36, 45, 46, 66, 67 in flight_search.py)

BG_COLOR = "#1d64aa"

window = Tk()
window.minsize(width=580, height=200)
img = PhotoImage(file="Cheap_Flight_Finder_Logo.png")
window.iconphoto(False, img)
window.title("CFF - Cheap Flight Finder")
window.config(bg=BG_COLOR, padx=5)

title_label = Label(text="Welcome to Cheap Flight Finder!✈️", bg=BG_COLOR,
                         pady=10, padx=20, justify="center", fg="white")
title_label.grid(row=0, column=0, columnspan=5)

from_dest_label = Label(text="From: ", bg=BG_COLOR, pady=5, padx=5, fg="white")
from_dest_label.grid(row=1, column=0)

to_dest_label = Label(text="To: ", bg=BG_COLOR, pady=10, padx=5, fg="white")
to_dest_label.grid(row=2, column=0)

from_dest_entry = Entry()
from_dest_entry.grid(row=1, column=1)
# from_dest_entry.config(fg="grey")
from_dest_entry.insert(0, "Travelling from...")

to_dest_entry = Entry()
to_dest_entry.grid(row=2, column=1)
# to_dest_entry.config(fg="grey")
to_dest_entry.insert(0, "Travelling to...")

d1_dates_label = Label(text="Departure date range: ", bg=BG_COLOR, pady=5, fg="white")
d1_dates_label.grid(row=1, column=2, padx=(50, 0))

d2_dates_label = Label(text="Return date range: ", bg=BG_COLOR, pady=10, fg="white")
d2_dates_label.grid(row=2, column=2, padx=(50, 0))

d1_start_date_entry = Entry(width=15)
d1_start_date_entry.grid(row=1, column=3)
# from_date_entry.config(fg="grey")
d1_start_date_entry.insert(0, "DD/MM/YYYY")

d1_end_date_entry = Entry(width=15)
d1_end_date_entry.grid(row=1, column=4, padx=(5, 0))
# to_date_entry.config(fg="grey")
d1_end_date_entry.insert(0, "DD/MM/YYYY")

d2_start_date_entry = Entry(width=15)
d2_start_date_entry.grid(row=2, column=3)
# from_date_entry.config(fg="grey")
d2_start_date_entry.insert(0, "DD/MM/YYYY")

d2_end_date_entry = Entry(width=15)
d2_end_date_entry.grid(row=2, column=4, padx=(5, 0))
# to_date_entry.config(fg="grey")
d2_end_date_entry.insert(0, "DD/MM/YYYY")

price_cutoff_label = Label(text="Price cutoff: ", bg=BG_COLOR, pady=5, fg="white")
price_cutoff_label.grid(row=3, column=0)

price_cutoff_entry = Entry()
price_cutoff_entry.grid(row=3, column=1)
# price_cutoff_entry.config(fg="grey")
price_cutoff_entry.insert(0, "Max price (BGN)")

email_label = Label(text="Email: ", bg=BG_COLOR, pady=10, fg="white")
email_label.grid(row=3, column=2, padx=(50, 5))

email_entry = Entry(width=32)
email_entry.grid(row=3, column=3, columnspan=2)
# email_entry.config(fg="grey")
email_entry.insert(0, "your_email@gmail.com")
# self.email_entry.insert(0, "Your email here...")

# date_note_label = Label(text="*Please take note that if no flights on the selected "
#                                   "dates match the price cutoff, computer will \nlook "
#                                   "for other dates, close to the ones selected.",
#                              bg=BG_COLOR, justify="left", fg="white")
# date_note_label.grid(row=6, column=0, columnspan=4, pady=(10, 5))
values = []
# button_pressed = False


def checkbutton_direct_value():
    return max_stops.get()


is_one_way1 = 0


def checkbutton_return_value():
    global is_one_way1
    is_one_way1 = is_one_way.get()
    if d2_dates_label["fg"] != "grey":
        d2_dates_label.config(fg="grey")
        d2_start_date_entry.config(state="disabled")
        d2_end_date_entry.config(state="disabled")
    else:
        d2_dates_label.config(fg="white")
        d2_start_date_entry.config(state="normal")
        d2_end_date_entry.config(state="normal")
    # return is_one_way.get()


max_stops = IntVar()
direct_flight_check = Checkbutton(master=window, text="Only Direct Flights",
                                  variable=max_stops, onvalue=0, bg=BG_COLOR,
                                  fg="white", selectcolor=BG_COLOR,
                                  offvalue=10, command=checkbutton_direct_value)
direct_flight_check.grid(row=4, column=1)
# print(max_stops)

is_one_way = BooleanVar()
is_one_way_check = Checkbutton(master=window, text="One-Way", variable=is_one_way,
                               onvalue=True, offvalue=False, bg=BG_COLOR, fg="white",
                               selectcolor=BG_COLOR, command=checkbutton_return_value)
is_one_way_check.grid(row=4, column=2)


def create_confirm_messagebox(from_dest, to_dest, recipient):
    messagebox.showinfo(title="Email sent", message=f"Email for a "
                                                    f"cheap flight "
                                                    f"{from_dest} - {to_dest}"
                                                    f" sent to {recipient}!")


def get_values():
    global max_stops
    global is_one_way1
    from_city = from_dest_entry.get()
    to_city = to_dest_entry.get()
    d1_start_date = d1_start_date_entry.get()
    d1_end_date = d1_end_date_entry.get()
    d2_start_date = d2_start_date_entry.get()
    d2_end_date = d2_end_date_entry.get()
    price_cutoff = price_cutoff_entry.get()
    email = email_entry.get()
    max_stops1 = checkbutton_direct_value()
    values.append(from_city)
    values.append(to_city)
    values.append(d1_start_date)
    values.append(d1_end_date)
    values.append(price_cutoff)
    values.append(email)
    values.append(max_stops1)
    values.append(is_one_way1)
    values.append(d2_start_date)
    values.append(d2_end_date)
    if d2_start_date_entry["state"] == "disabled":
        del values[8:9]
    # print(len(values))
    # len(values) = 7 (0,1,2,3,4,5,6)

    # try:
    new_flight_search = FlightSearch(values[0])
    # print(values)
    dep_start_date = values[2]
    dep_end_date = values[3]
    try:
        price_cutoff = int(values[4])
    except ValueError:
        messagebox.showwarning(title="Invalid Price Cutoff!", message="Please enter a valid price cutoff.")
    else:
        print(f"Values: {values}")
        try:
            data_for_flight_data = new_flight_search.search_query(values[1], dep_start_date,
                                                                  dep_end_date, values[6],
                                                                  values[8], values[9])
            # if len(data_for_flight_data) == 0:
            #     messagebox.showwarning(title="No such flights found!", message=
            #                            "We could not find flights matching the search "
            #                            "query. Please change some of the parameters.")
        except IndexError:
            data_for_flight_data = new_flight_search.search_query(values[1], dep_start_date, dep_end_date,
                                                                  values[6])
        try:
            flight_data = FlightData(data_for_flight_data, price_cutoff)
        except IndexError:
            messagebox.showwarning(title="No such flights found!", message="We could not find flights matching the search "
                                                                           "query. Please change some of the parameters.")
            print(f"No cheap flights to {values[1]} found around the selected dates.")
            # except IndexError:
            #     messagebox.showwarning(title="Fields left unfilled!", message="Please fill "
            # "in all fields!")
        else:
            if flight_data.deal_present():
                print("Flight deal present")
                notif_manager = NotificationManager(flight_data)

                # Uncomment these two lines to get an immediate email with the cheapest flight:
                # notif_manager.send_email(values[5])
                # create_confirm_messagebox(values[0], values[1], values[5])

                # Uncomment this line to get an immediate messagebox with the cheapest flight:
                notif_manager.show_answer_window()
            else:
                messagebox.showwarning(title="No such flights found!",
                                       message="We could not find flights matching the search "
                                               "query. Please change some of the parameters.")
                print(f"No cheap flights to {values[1]} found around the selected dates.")
    values.clear()


enter_data_button = Button(text="Search", command=get_values)
enter_data_button.grid(row=4, column=3, pady=10, columnspan=2)

canvas = Canvas(width=300, height=150, bg=BG_COLOR, highlightthickness=0)
logo_img = PhotoImage(file="cheap_flights_logo_small_v3.png")
canvas.create_image((150, 75), image=logo_img)
canvas.grid(row=5, column=0, columnspan=5)


window.mainloop()



# ################################################################################
# VERSION 3: WITHOUT GUI AND NOT USING GOOGLE SHEETS (PANDAS AND CSV):
# (NOTE: For this version, uncomment also lines 33, 36, 45, 46, 66, 67
# and comment lines 32, 35, 43, 44, 64, 65 in flight_search.py)

# data_manager = Pandas_Data()
# new_flight_search = FlightSearch("Milan")
#
# # data_manager.update_row(3, "Madrid", 80)
# # data_manager.add_row("Seville", 100)
# # data_manager.add_row("Amsterdam", 120)
# # data_manager.add_row("Reykjavik", 100)
# # data_manager.update_row(1, "Reykjavik", 100)
# # data_manager.update_row(2, "Madrid", 60)
# # data_manager.add_row("Sofia", 30)
# # data_manager.add_row("Eindhoven", 100)
# # data_manager.add_row("Palermo", 50)
# # data_manager.add_row("Catania", 50)
# # data_manager.add_row("Vienna", 80)
# # data_manager.add_row("Madeira", 100)
# # data_manager.add_row("Porto", 50)
# # data_manager.add_row("Bratislava", 50)
# # data_manager.delete_row(8)
# # data_manager.clear_all()
#
# date_now = datetime.now().date()
# # Searching for a return flight in 1-3 months time:
# departure_date_start = (date_now + timedelta(days=30)).strftime("%d/%m/%Y")
# departure_date_end = (date_now + timedelta(days=90)).strftime("%d/%m/%Y")
# # By default: Search for min 2 and max 6 nights spent
# nights_spent_min = 2
# nights_spent_max = 6
# recipient = "pumpalmanatarka@gmail.com"
# # departure_date_start = input("Please enter a departure date in this format: DD/MM/YYYY: ")
# # departure_date_end = input("Please enter an arrival date in this format: DD/MM/YYYY: ")
# # recipient = input("Please enter your email: ")
#
# for city in data_manager.cities:
#     # budget = data_manager.cutoffs[data_manager.cities.index(city)]
#     data_for_flight_data = new_flight_search.search_query(city, departure_date_start, departure_date_end, 10,
#                                                           nights_spent_min, nights_spent_max)
#     price_cutoff = data_manager.cutoffs[data_manager.cities.index(city)]
#     flight_data = FlightData(data_for_flight_data, price_cutoff)
#
#     if flight_data.deal_present():
#         notif_manager = NotificationManager(flight_data)
#         notif_manager.send_email(recipient)
#
#     else:
#         print(f"No cheap flights to {city} found around the selected dates.")
