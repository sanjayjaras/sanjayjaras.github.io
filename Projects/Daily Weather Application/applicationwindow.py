import json
import tkinter as tk
from tkinter import ttk

import auto_complete_entry as ac


def load_cities(country: str):
    result = {}
    with open("city.list.json", "r", encoding="UTF-8") as cities_file:
        cities = json.load(cities_file)
        city_options = {}
        for city in cities:
            if city["name"] is not None and len(city["name"]) > 1 and city["country"] == country:
                city_options[city["name"] + " - " + city["country"]] = city["id"]
        for key in sorted(city_options.keys()):
            result[key] = city_options[key]
    return result


def load_countries():
    result = set()
    with open("city.list.json", "r", encoding="UTF-8") as cities_file:
        countries = json.load(cities_file)
        city_options = {}
        for city in countries:
            if city["country"] is not None and len(city["country"]) > 1:
                result.add(city["country"])
    return sorted(result)


countries = load_countries()
cities = load_cities("US")

list_of_cities_for_auto_complete = list(cities.keys())


class ApplicationWindow:

    def __init__(self, app_window, callback_function):
        self.app_window = app_window
        self.app_window.callback_function = callback_function
        self.app_window.choice = tk.IntVar()
        self.app_window.choice.set(1)

        self.app_window.country = tk.StringVar()
        self.app_window.country.set("US")
        self.app_window.city_id = None
        self.app_window.city_name = tk.StringVar()
        self.app_window.zipcode = tk.StringVar()
        # set window size
        app_window.geometry("600x200")
        # set window title
        app_window.title("Weather Application")
        # row number in grid
        row = 0

        # set app title
        app_window.app_title = tk.Label(app_window, text="Get weather forecast...").grid(row=row,
                                                                                         column=2)
        row += 1
        app_window.app_title = tk.Label(app_window, text="Country").grid(row=row, column=1)
        app_window.combo_country = ttk.Combobox(app_window, values=countries, textvariable=self.app_window.country,
                                                width=50
                                                )
        app_window.combo_country.grid(row=row, column=2)
        app_window.combo_country.bind("<<ComboboxSelected>>", self.country_change)

        row += 1
        tk.Radiobutton(app_window, text="City Name", variable=self.app_window.choice, value=1,
                       command=self.city_zip_option_selected).grid(
            row=row,
            column=1,
            pady=10)

        # ,       textvariable=self.app_window.city_name, width=50
        app_window.text_city_name = ac.AutoCompleteEntry(list_of_cities_for_auto_complete, app_window, width=50)
        app_window.text_city_name.grid(row=row, column=2, pady=10)
        self.app_window.city_name = app_window.text_city_name.var

        row += 1
        tk.Radiobutton(app_window, text="Zip Code", variable=self.app_window.choice, value=2,
                       command=self.city_zip_option_selected).grid(
            row=row,
            column=1,
            pady=1)
        app_window.text_zipcode = tk.Entry(app_window, width=50, textvariable=self.app_window.zipcode)
        app_window.text_zipcode.grid(row=row, column=2)
        self.city_zip_option_selected()

        row += 1
        tk.Button(app_window, text="Get Forecast",
                  command=self.get_forecast).grid(row=row, column=2)

    def city_zip_option_selected(self):
        if self.app_window.choice.get() is 1:
            self.app_window.text_city_name.insert('end', "")
            self.app_window.text_city_name.configure(state="normal")
            self.app_window.text_zipcode.configure(state="disabled")
            self.app_window.zipcode.set("")
            self.app_window.text_city_name.insert('end', "")
        else:
            self.app_window.text_city_name.insert('end', "")
            self.app_window.text_city_name.configure(state="disabled")
            self.app_window.city_name.set("")
            self.app_window.text_zipcode.configure(state="normal")
            self.app_window.text_city_name.insert('end', "")

    def get_forecast(self):
        print("Choice:{} City:{} Zip Code:{}".format(self.app_window.choice, self.app_window.city_name,
                                                     self.app_window.zipcode))

        choice = self.app_window.choice
        city = self.app_window.city_name
        zip = self.app_window.zipcode
        if choice.get() is 1:
            if city is None or len(city.get()) is 0 or city.get() not in cities:
                print("Please enter valid city name...")
            else:
                print("Entered city:{} and City Id: {}".format(city.get(), cities[city.get()]))
                self.app_window.callback_function({"id": str(cities[city.get()])})
        if choice.get() is 2:
            if zip is None or len(zip.get()) is 0:
                print("Please enter valid zip code...")
            else:
                self.app_window.callback_function({"zip": zip.get() + "," + self.app_window.country.get()})

    def country_change(self, event):
        global cities
        cities = load_cities(self.app_window.country.get())
        list_of_cities_for_auto_complete.clear()
        list_of_cities_for_auto_complete.extend(list(cities.keys()))
