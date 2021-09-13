import requests
from bs4 import BeautifulSoup

base_url = "http://www.howstat.com/cricket/Statistics/Matches/"


def find_match_summary(table, dt, team1, team2):
    trs = table.find_all("tr")
    for tr in trs:
        tds = tr.find_all("td")
        if tds[0].text.isdigit() and tds[1].text.strip() == dt:
            teams = tds[2].text.split("v.")
            teams = [x.strip() for x in teams]
            if (
                team1 == teams[0]
                or team1 == teams[1]
                or team2 == teams[0]
                or team2 == teams[1]
            ):
                return [
                    tds[3].text.strip(),
                    tds[4].text.strip(),
                    tds[5].find("a")["href"],
                ]
    return []


def get_match_summary(dt, team1, team2):
    grp = str(dt.year) + "0101" + str(dt.year) + "1231"
    url = base_url + "MatchList.asp?Group=" + grp
    req = requests.get(url, None)
    soup = BeautifulSoup(req.content, "html.parser")
    table = soup.find("table", {"class": "TableLined"})
    summary = find_match_summary(table, dt.strftime("%d/%m/%Y"), team1, team2)
    return summary


def get_scorecard(matchurl):
    url = base_url + matchurl
    req = requests.get(url, None)
    soup = BeautifulSoup(req.content, "html.parser")
    scorecard = soup.find_all("table")[5].find_all("table")[1]
    batting = []
    bowling = []
    rows_for_table2 = scorecard.find_all("tr")
    inning_no = 0
    for row in rows_for_table2:
        try:
            first_cell = row.find_all("td")[0].text
            if "Innings" in first_cell:
                inning_no += 1
                batting_in_progress = True
            elif "Extras" in first_cell:
                batting_in_progress = False
            elif "Bowling" in first_cell:
                bl_rows = row.find_all("tr")[1:]
                for row in bl_rows:
                    bowling.append(
                        [inning_no]
                        + [td.get_text().strip() for td in row.findAll("td")]
                    )
            elif batting_in_progress:
                batting.append(
                    [inning_no] + [td.get_text().strip() for td in row.findAll("td")]
                )
        except IndexError as e:
            print("Error occured for Match url:", url, e)
    return batting, bowling
