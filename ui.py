from tkinter import *
from tkinter import messagebox

BG_COLOR = "#1d64aa"


def create_confirm_messagebox(from_city, to_city, email):
    messagebox.showinfo(title="Email sent", message=f"Email for a "
                                                    f"cheap return flight "
                                                    f"{from_city} - {to_city}"
                                                    f" sent to {email}!")


class UI:
    def __init__(self):
        self.window = Tk()
        self.window.minsize(width=470, height=200)
        self.window.title("Cheap Flight Finder")
        self.window.config(bg=BG_COLOR, padx=10)

        self.title_label = Label(text="Welcome to Cheap Flight Finder!✈️", bg=BG_COLOR,
                            pady=10, padx=20, justify="center", fg="white")
        self.title_label.grid(row=0, column=0, columnspan=4)

        self.from_dest_label = Label(text="From: ", bg=BG_COLOR, pady=5, padx=5, fg="white")
        self.from_dest_label.grid(row=1, column=0)

        self.to_dest_label = Label(text="To: ", bg=BG_COLOR, pady=10, padx=5, fg="white")
        self.to_dest_label.grid(row=2, column=0)

        self.from_dest_entry = Entry()
        self.from_dest_entry.grid(row=1, column=1)
        # from_dest_entry.config(fg="grey")
        self.from_dest_entry.insert(0, "Travelling from...")

        self.to_dest_entry = Entry()
        self.to_dest_entry.grid(row=2, column=1)
        # to_dest_entry.config(fg="grey")
        self.to_dest_entry.insert(0, "Travelling to...")

        self.from_date_label = Label(text="Departure date*: ", bg=BG_COLOR, pady=5, fg="white")
        self.from_date_label.grid(row=1, column=2, padx=(50, 5))

        self.to_date_label = Label(text="Return date*: ", bg=BG_COLOR, pady=10, fg="white")
        self.to_date_label.grid(row=2, column=2, padx=(50, 5))

        self.from_date_entry = Entry()
        self.from_date_entry.grid(row=1, column=3)
        # from_date_entry.config(fg="grey")
        self.from_date_entry.insert(0, "DD/MM/YYYY")

        self.to_date_entry = Entry()
        self.to_date_entry.grid(row=2, column=3)
        # to_date_entry.config(fg="grey")
        self.to_date_entry.insert(0, "DD/MM/YYYY")

        self.price_cutoff_label = Label(text="Price cutoff: ", bg=BG_COLOR, pady=5, fg="white")
        self.price_cutoff_label.grid(row=3, column=0)

        self.price_cutoff_entry = Entry()
        self.price_cutoff_entry.grid(row=3, column=1)
        # price_cutoff_entry.config(fg="grey")
        self.price_cutoff_entry.insert(0, "Max return price (lv.)")

        self.email_label = Label(text="Email: ", bg=BG_COLOR, pady=10, fg="white")
        self.email_label.grid(row=3, column=2, padx=(50, 5))

        self.email_entry = Entry()
        self.email_entry.grid(row=3, column=3)
        # email_entry.config(fg="grey")
        self.email_entry.insert(0, "simeon.dachevv@gmail.com")
        # self.email_entry.insert(0, "Your email here...")

        self.date_note_label = Label(text="*Please take note that if no flights on the selected "
                                     "dates match the price cutoff, computer will \nlook "
                                     "for other dates, close to the ones selected.",
                                bg=BG_COLOR, justify="left", fg="white")
        self.date_note_label.grid(row=6, column=0, columnspan=4, pady=(10, 5))
        self.enter_data_button = Button(text="Search", command=self.get_values)
        self.enter_data_button.grid(row=4, column=0, columnspan=4, pady=10)

        self.canvas = Canvas(width=300, height=150, bg=BG_COLOR, highlightthickness=0)
        logo_img = PhotoImage(file="cheap_flights_logo_small_v3.png")
        self.canvas.create_image((150, 75), image=logo_img)
        self.canvas.grid(row=5, column=0, columnspan=4)

        self.from_city = NONE
        self.to_city = NONE
        self.from_date = NONE
        self.to_date = NONE
        self.price_cutoff = NONE
        self.email = NONE
        self.button_pressed = False
        # while True:
        #     if self.button_pressed:
        #         create_confirm_messagebox()
        #         break
        #     self.window.mainloop()

        self.window.mainloop()

    def get_values(self):
        self.from_city = self.from_dest_entry.get()
        self.to_city = self.to_dest_entry.get()
        self.from_date = self.from_date_entry.get()
        self.to_date = self.to_date_entry.get()
        self.price_cutoff = self.price_cutoff_entry.get()
        self.email = self.email_entry.get()
        self.button_pressed = True
        # self.values = []
        # values.extend([from_city, to_city, from_date, to_date, price_cutoff, email])
        # print(values)







