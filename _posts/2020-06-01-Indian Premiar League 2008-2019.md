---
title: "Indian Premier League 2008-2019"
date: 2020-06-01
tags:
 - Python
 - Jupyter Notebook
 
excerpt: "EDA of Indian Premier League 2008-2019"
header:
  overlay_image: "/Projects/Indian Premiar Leage 2008-2019/assets/image1.png"
  overlay_filter: 0.3 # same as adding an opacity of 0.3 to a black background
  teaser: "/Projects/Indian Premiar Leage 2008-2019/assets/image1.png"
  actions:
    - label: "Go to GitHub Repository"
      url: "https://github.com/sanjayjaras/sanjayjaras.github.io/tree/master/Projects/Indian%20Premiar%20Leage%202008-2019"
---




# Indian Premier League 2008-2019
## EDA of Indian Premier League 2008-2019



The Indian Premier League (IPL) is a professional Twenty20 cricket league in Indi. It is typically contested during March through May of every year by eight teams representing eight different cities in India. The Board of Control for Cricket in India (BCCI) started the league in 2008. The IPL has a particular timeslot in ICC(Internationational Cricket Council) Future Tours Programme. The IPL is the most-attended cricket league in the world. In 2014 IPL is ranked sixth by average attendance among all sports leagues. The brand value of the IPL in 2019 was ₹475 billion (US$6.7 billion), according to Duff & Phelps. According to BCCI, the 2015 IPL season contributed ₹11.5 billion (US$160 million) to the GDP of the Indian economy.
The dataset I got from Kaggle.com has ball by ball information of all seasons of IPL that happened from 2008 through 2019. This dataset contains a total of 751 matches played. This dataset contains one CSV file for each game. This data needs to be used combinedly for performing analysis; for this, we need to combine data from all CSVs. Each CSV has the following columns
1. Innings: Numeric field representing first or second innings.
2. Over: Numeric field representing ball number from each innings.
3. Batting Team: String field representing the name of the batting team.
4. Player: String field representing the name of the player batting.
5. Non Striker: String field representing the name of the player present at the non-striking end.
6. Baller: String field representing the name of the bowler.
7. Runs: Numeric field representing the number of runs scored by a batsman.
8. Extra: Numeric field representing the number of runs fielding team conceded extras.


The needs to be cleaned if required. This dataset can be used to answer different questions.  Some of the questions are as follows. 

1. Economical bowler in each season(calculate an average per Over)
2. Economical bowler in from all seasons(calculate an average per Over)
3. Economical bowler in the powerplay(calculate an average per Over)
4. Economical bowler in the death overs(calculate an average per Over)
5. Opening batsman that scored most runs in each season
6. Opening batsman that scored most runs in all seasons
7. Middle-order batsman that scored most runs in each season
8. Middle-order batsman that scored most runs in all seasons
9. The most attacking batsman in each season(Strike rate per 100 balls)
10. The most attacking batsman in all season(Strike rate per 100 balls)
11. The strike rate for a batsman against some bowler.

## Reference:
https://www.kaggle.com/sagara9595/indian-premier-league-20082019