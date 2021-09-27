import json
import requests as rq
import serviceutils as su


class WeatherService:
    def __init__(self):
        self.selected_country = "US"
        self.api_key = "adb0baa3704cfe9e9eca733ff09f3ade"
        self.url = "https://api.openweathermap.org/data/2.5/forecast"

    def get_menu_choice(self) -> int:
        su.print_cyan("*" * 100)
        welcome_msg = "Welcome to Weather Channel"
        su.print_cyan("{:^100}".format(welcome_msg))
        su.print_cyan("*" * 100)
        su.print_cyan("\t1. Weather By Zip Code")
        su.print_cyan("\t2. Weather By City")
        su.print_cyan("\t3. Change Country ({})".format(self.selected_country))
        su.print_cyan("\t0. Exit")
        while True:
            choice = input("\tEnter choice:")
            if not choice.isnumeric() or int(choice) < 0 or int(choice) > 3:
                su.print_red("\tInvalid choice....")
            else:
                break
        return int(choice)

    def change_country(self):
        country = input("Please enter 2 letter country code(e.g. US):")
        if country is None or len(country) < 1:
            su.print_red("\t Invalid country code")
        else:
            self.selected_country = country.upper()

    def get_weather_by_zip(self):
        zip_code = input("\tEnter zip code:")
        if zip_code is None or len(zip_code) < 1:
            su.print_red("Invalid Zip-code")
        else:
            param = {"zip": zip_code + "," + self.selected_country}
            self.invoke_service(param)

    def get_weather_by_city(self):
        city_name = input("\tEnter city name:")
        if city_name is None or len(city_name) < 1:
            su.print_red("Invalid City Name")
        else:
            param = {"city": city_name + "," + self.selected_country}
            self.invoke_service(param)

    def invoke_service(self, input: dict):
        params = {"appid": self.api_key}
        if "city" in input:
            params["q"] = input["city"]
        else:
            params["zip"] = input["zip"]
        print("Request params:", params)
        try:
            response = rq.get(url=self.url, params=params)
        except rq.exceptions.RequestException as e:
            su.print_red("\tSomething went bad..\n\tError Details:{}".format(e))
        else:
            print("Response:{}".format(json.dumps(response.json())))
            self.show_result(response.json())

    def show_result(self, response_json_obj: dict):
        if response_json_obj["cod"] == "200":
            su.print_cyan("=" * 160)
            city_name = response_json_obj["city"]["name"]
            su.print_green("\t{:<8}:{:<30}{:<8}:{:<30}".format("City", city_name, "Country", self.selected_country))
            sunrise_user_time = su.get_time_hhmmsszzz(
                su.convert_time_local_from_epoch(response_json_obj["city"]["sunrise"]))
            sunset_user_time = su.get_time_hhmmsszzz(
                su.convert_time_local_from_epoch(response_json_obj["city"]["sunset"]))
            su.print_green(
                "\t{:<8}:{:<30}{:<8}:{:<30}".format("Sunrise", sunrise_user_time, "Sunset", sunset_user_time))

            sunrise_local_time = su.get_time_hhmmss(
                su.convert_time_from_epoch(response_json_obj["city"]["sunrise"], response_json_obj["city"]["timezone"]))
            sunset_local_time = su.get_time_hhmmss(
                su.convert_time_from_epoch(response_json_obj["city"]["sunset"], response_json_obj["city"]["timezone"]))
            su.print_green(
                "\t{:<8}:{:<30}{:<8}:{:<30}".format("Sunrise", sunrise_local_time, "Sunset", sunset_local_time))
            su.print_cyan("-" * 160)
            su.print_cyan("{:^150}".format("\tWeather 5 day / 3 hour forecast data"))
            count = response_json_obj["cnt"]
            su.print_cyan("-" * 160)
            print_details_row("Date Time", "forecast", "Temp", "Min.", "Max.", "Rain", "Snow", "Pressure", "Wind-Speed",
                              "Wind-Direction", "Sea-Level", "Ground-Level", "Humidity")
            su.print_cyan("-" * 160)
            for i in range(1, count):
                date = response_json_obj["list"][i]["dt_txt"]
                temp = su.kelvin_to_fehrenheit(response_json_obj["list"][i]["main"]["temp"])
                min_temp = su.kelvin_to_fehrenheit(response_json_obj["list"][i]["main"]["temp_min"])
                max_temp = su.kelvin_to_fehrenheit(response_json_obj["list"][i]["main"]["temp_max"])
                pressure = response_json_obj["list"][i]["main"]["pressure"]
                sea_level = response_json_obj["list"][i]["main"]["sea_level"]
                grnd_level = response_json_obj["list"][i]["main"]["grnd_level"]
                humidity = response_json_obj["list"][i]["main"]["humidity"]
                weather = response_json_obj["list"][i]["weather"][0]["description"]
                wind_speed = response_json_obj["list"][i]["wind"]["speed"]
                wind_dir = su.degree_to_direction(response_json_obj["list"][i]["wind"]["deg"])
                rain = "-"
                if "rain" in response_json_obj["list"][i]:
                    rain = str(response_json_obj["list"][i]["rain"]["3h"]) + "mm"
                snow = "-"
                if "snow" in response_json_obj["list"][i]:
                    snow = str(response_json_obj["list"][i]["snow"]["3h"])

                print_details_row(date, weather, temp, min_temp, max_temp, rain, snow, str(pressure) + "hPa",
                                  str(wind_speed) + "mph",
                                  wind_dir, str(sea_level) + "hPa", str(grnd_level) + "hPa", str(humidity) + "%")

            su.print_cyan("=" * 160)

        else:
            su.print_red("Something went bad: {}".format(response_json_obj["message"]))


def print_details_row(dt, forecast, temp, min_temp, max_temp, rain, snow, pressure, wind_speed, wind_dir, sea_level,
                      grnd_level, humidity):
    su.print_green(
        "\t{:<24}{:<25}{:<8}{:<8}{:<8}{:<7}{:<7}{:<12}{:<15}{:<10}{:<10}{:<14}{:<5}".format(dt, forecast, temp,
                                                                                            min_temp, max_temp,
                                                                                            rain, snow, wind_speed,
                                                                                            wind_dir, pressure,
                                                                                            sea_level,
                                                                                            grnd_level, humidity))


def main():
    service = WeatherService()
    choice = 1
    while choice != 0:
        choice = service.get_menu_choice()
        if choice == 0:
            print_green("Thank you...")
        elif choice == 1:
            service.get_weather_by_zip()
        elif choice == 2:
            service.get_weather_by_city()
        elif choice == 3:
            service.change_country()


if __name__ == '__main__':
    main()
