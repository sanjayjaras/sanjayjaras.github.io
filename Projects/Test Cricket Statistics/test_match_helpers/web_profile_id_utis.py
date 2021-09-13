from bs4 import BeautifulSoup
import requests
import pandas as pd
import Levenshtein as lv

base_url = "https://www.cricapi.com/players/?search="


def get_profile_ids(player_name):
    url = base_url + player_name
    req = requests.get(url, None)
    soup = BeautifulSoup(req.content, "html.parser")
    anchors = soup.body.findAll("a", {"itemprop": "url"})
    result = []
    for anchor in anchors:
        pid = anchor["href"].split("/")[-1]
        result.append(
            [anchor.find("h2").contents[0], pid, anchor.find("small").contents[0]]
        )
    return result


def find_closest_short_name(player, profiles):
    names = player.split()
    for target_player in profiles:
        if player.upper() == target_player[0]:
            return target_player

        target_names = target_player[2].split()
        match = False
        if names[-1] == target_names[-1]:  # last name matches
            match = True
            for i in range(len(names[0])):
                if not target_names[i].startswith(names[0][i]):
                    match = False
                    break
        if match:
            return target_player
    return None


def find_closest_fuzzy_match(player, profiles):
    mini = 999
    closest_match = ""
    for target_player in profiles:
        dist = lv.distance(player.upper(), target_player[2].upper())
        if dist < mini:
            mini = dist
            closest_match = target_player
        if mini == 0:
            break
    return closest_match


def find_Profile_id(player, profiles):
    if len(profiles) == 1:
        return profiles[0]
    else:  # got multiple profiles
        profile = find_closest_short_name(player, profiles)
        if profile is None:
            profile = find_closest_fuzzy_match(player, profiles)
    return profile


def get_profile_id(player):
    pids = get_profile_ids(player)
    if len(pids) != 1:
        names = player.split()
        pids = get_profile_ids(names[-1])
        profile = find_Profile_id(player, pids)
    else:
        profile = pids[0]
    return profile


# print(get_profile_id("IR Bell"))
