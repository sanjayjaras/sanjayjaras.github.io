import json
import time
import tkinter as tk

import applicationwindow as aw
import requests as rq

api_key = "adb0baa3704cfe9e9eca733ff09f3ade"
url = "https://api.openweathermap.org/data/2.5/forecast"


def convert_time_local_from_epoch(epoch_time: int) -> str:
    local_time = epoch_time
    return time.localtime(local_time)


def convert_time_from_epoch(epoch_time: int, time_diff: int) -> str:
    local_time = epoch_time + time_diff
    return time.gmtime(local_time)


def get_time_hhmmsszzz(time_tuple) -> str:
    return "%02d:%02d:%02d %s" % (time_tuple.tm_hour, time_tuple.tm_min, time_tuple.tm_sec, time_tuple.tm_zone)


def get_time_hhmmss(time_tuple) -> str:
    return "%02d:%02d:%02d Local Time" % (time_tuple.tm_hour, time_tuple.tm_min, time_tuple.tm_sec)


def get_time_mmddhhmm(time_tuple: tuple) -> str:
    return "%02d/%02 %02d:%02d:%02d" % (
        time_tuple.tm_mon, time_tuple.tm_mday, time_tuple.tm_hour, time_tuple.tm_min)


def invoke_service(input: dict):
    params = {"appid": api_key}
    if "id" in input:
        params["id"] = input["id"]
    else:
        params["zip"] = input["zip"]
    print("Request params:", params)
    response = rq.get(url=url, params=params)
    print("Response:{}".format(json.dumps(response.json())))
    show_result(response.json())


def show_result(response_json_obj: dict):
    if response_json_obj["cod"] == "200":
        print("Successful...")
        print("City:" + response_json_obj["city"]["name"])
        # local Time
        print("Local Time:")
        print("Sunrise: " + get_time_hhmmss(
            convert_time_from_epoch(response_json_obj["city"]["sunrise"], response_json_obj["city"]["timezone"])))
        print("Sunset: " + get_time_hhmmss(
            convert_time_from_epoch(response_json_obj["city"]["sunset"], response_json_obj["city"]["timezone"])))

        # System Time
        print("Sunrise: " + get_time_hhmmsszzz(convert_time_local_from_epoch(response_json_obj["city"]["sunrise"])))
        print("Sunset: " + get_time_hhmmsszzz(convert_time_local_from_epoch(response_json_obj["city"]["sunset"])))



    else:
        print("Failure...")


def main():
    global root
    root = tk.Tk()
    application = aw.ApplicationWindow(root, invoke_service)
    root.mainloop()


if __name__ == '__main__':
    main()
