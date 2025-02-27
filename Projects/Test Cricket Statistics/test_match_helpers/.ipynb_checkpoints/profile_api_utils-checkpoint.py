import requests
import pandas as pd
import json


def get_base_url():
    with open("apikey.json") as f:
        keys = json.load(f)
        apikey = keys["cricapi_key"]
    return "http://cricapi.com/api/playerStats?apikey=" + apikey + "&pid="


def parse_json(json):
    batting = {}
    bowling = {}
    if (
        "data" in json
        and "batting" in json["data"]
        and "tests" in json["data"]["batting"]
    ):
        batting = json["data"]["batting"]["tests"]
    if (
        "data" in json
        and "bowling" in json["data"]
        and "tests" in json["data"]["bowling"]
    ):
        bowling = json["data"]["bowling"]["tests"]
    return batting, bowling


def get_profile(pid):

    resp = requests.get(get_base_url() + pid)
    if resp.status_code != 200:
        print("Error in getting Player profile Id...", resp.status_code)
        return {}, {}
    else:
        return parse_json(resp.json())


# batting, bowling = get_profile("55882")
# print(batting)
# print(bowling)

# json = {'pid': 35320, 'profile': "\n\nSachin Tendulkar has been the most complete batsman of his time, the most prolific runmaker of all time, and arguably the biggest cricket icon the game has ever known. His batting was based on the purest principles: perfect balance, economy of movement, precision in stroke-making, and that intangible quality given only to geniuses - anticipation. If he didn't have a signature stroke - the upright, back-foot punch comes close - it's because he was equally proficient at each of the full range of orthodox shots (and plenty of improvised ones as well) and can pull them out at will.  \n\n", 'imageURL': 'https://www.cricapi.com/playerpic/35320.jpg', 'battingStyle': 'Right-hand bat', 'bowlingStyle': 'Right-arm offbreak, Legbreak googly', 'majorTeams': 'India,Asia XI,Mumbai,Mumbai Indians,Yorkshire', 'currentAge': '44 years 186 days', 'born': 'April 24, 1973, Bombay (now Mumbai), Maharashtra', 'fullName': 'Sachin Ramesh Tendulkar', 'name': 'Sachin Tendulkar', 'country': 'India', 'playingRole': 'Top-order batsman', 'v': '2', 'data': {'bowling': {'listA': {'10': '0', '5w': '2', '4w': '4', 'SR': '50.8', 'Econ': '4.97', 'Ave': '42.17', 'BBM': '5/32', 'BBI': '5/32', 'Wkts': '201', 'Runs': '8478', 'Balls': '10230', 'Inns': '', 'Mat': '551'}, 'firstClass': {'10': '0', '5w': '0', '4w': '', 'SR': '107.1', 'Econ': '3.45', 'Ave': '61.74', 'BBM': '', 'BBI': '3/10', 'Wkts': '71', 'Runs': '4384', 'Balls': '7605', 'Inns': '', 'Mat': '310'}, 'T20Is': {'10': '0', '5w': '0', '4w': '0', 'SR': '15.0', 'Econ': '4.80', 'Ave': '12.00', 'BBM': '1/12', 'BBI': '1/12', 'Wkts': '1', 'Runs': '12', 'Balls': '15', 'Inns': '1', 'Mat': '1'}, 'ODIs': {'10': '0', '5w': '2', '4w': '4', 'SR': '52.2', 'Econ': '5.10', 'Ave': '44.48', 'BBM': '5/32', 'BBI': '5/32', 'Wkts': '154', 'Runs': '6850', 'Balls': '8054', 'Inns': '270', 'Mat': '463'}, 'tests': {'10': '0', '5w': '0', '4w': '0', 'SR': '92.1', 'Econ': '3.52', 'Ave': '54.17', 'BBM': '3/14', 'BBI': '3/10', 'Wkts': '46', 'Runs': '2492', 'Balls': '4240', 'Inns': '145', 'Mat': '200'}}, 'batting': {'listA': {'50': '114', '100': '60', 'St': '0', 'Ct': '175', '6s': '', '4s': '', 'SR': '', 'BF': '', 'Ave': '45.54', 'HS': '200*', 'Runs': '21999', 'NO': '55', 'Inns': '538', 'Mat': '551'}, 'firstClass': {'50': '116', '100': '81', 'St': '0', 'Ct': '186', '6s': '', '4s': '', 'SR': '', 'BF': '', 'Ave': '57.84', 'HS': '248*', 'Runs': '25396', 'NO': '51', 'Inns': '490', 'Mat': '310'}, 'T20Is': {'50': '0', '100': '0', 'St': '0', 'Ct': '1', '6s': '0', '4s': '2', 'SR': '83.33', 'BF': '12', 'Ave': '10.00', 'HS': '10', 'Runs': '10', 'NO': '0', 'Inns': '1', 'Mat': '1'}, 'ODIs': {'50': '96', '100': '49', 'St': '0', 'Ct': '140', '6s': '195', '4s': '2016', 'SR': '86.23', 'BF': '21367', 'Ave': '44.83', 'HS': '200*', 'Runs': '18426', 'NO': '41', 'Inns': '452', 'Mat': '463'}, 'tests': {'50': '68', '100': '51', 'St': '0', 'Ct': '115', '6s': '69', '4s': '', 'SR': '', 'BF': '', 'Ave': '53.78', 'HS': '248*', 'Runs': '15921', 'NO': '33', 'Inns': '329', 'Mat': '200'}}}, 'ttl': 2, 'provider': {'source': 'Various', 'url': 'https://cricapi.com/', 'pubDate': '2020-07-19T14:50:59.730Z'}, 'creditsLeft': 250}
# batting, bowling = parse_json(json)
# df_profile_bat = pd.DataFrame()
# df_profile_bat=df_profile_bat.append(batting, ignore_index=True)
# df_profile_bowl = pd.DataFrame()
# df_profile_bowl=df_profile_bowl.append(bowling, ignore_index=True)
# print(df_profile_bat)
# print(df_profile_bowl)

