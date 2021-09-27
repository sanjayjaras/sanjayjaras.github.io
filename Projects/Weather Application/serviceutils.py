import time
import timezonefinder


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


def print_red(message: str): print("\033[91m {}\033[00m".format(message))


def print_green(message: str): print("\033[92m {}\033[00m".format(message))


def print_cyan(message: str): print("\033[96m {}\033[00m".format(message))


def kelvin_to_fehrenheit(in_kelvin: float) -> str:
    return "%.0f\N{DEGREE SIGN}F" % ((in_kelvin - 273.15) * 9 / 5 + 32)


def degree_to_direction(degree) -> str:
    sectors = {1: "N", 2: "NNE", 3: "NE", 4: "ENE", 5: "E", 6: "ESE", 7: "SE", 8: "SSE", 9: "S", 10: "SSW", 11: "SW",
               12: "WSW", 13: "W", 14: "WNW", 15: "NW", 16: "NNW", 17: "N"}
    index = degree % 360
    index = round(index / 22.5, 0) + 1
    return sectors[index]
