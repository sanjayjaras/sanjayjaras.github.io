---
title: "Test Cricket Statistics"
date: 2020-06-01
tags:
 - Python
 - Jupyter Notebook
 
excerpt: "Test Cricket Statistics: Data Preparation and Basic EDA"
header:
  overlay_image: "/Projects/Test Cricket Statistics/assets/image1.jpg"
  overlay_filter: 0.3 # same as adding an opacity of 0.3 to a black background
  teaser: "/Projects/Test Cricket Statistics/assets/image1.jpg"
  actions:
    - label: "Go to GitHub Repository"
      url: "https://github.com/sanjayjaras/sanjayjaras.github.io/tree/master/Projects/Test%20Cricket%20Statistics"
---




# Test Cricket Statistics
## Test Cricket Statistics: Data Preparation and Basic EDA

Test Cricket Statistics - The test matches are long format of cricket. Test Match is played for 5 days. Each team gets 2 innings.Every match can have 4 inning max, however some matches are finished in 3 innings. Under this project the data is loaded from three different data sources
  * Yaml Files
  * Website
  * Api
  
### Yaml files: 
  Yaml files are extracted from zip file. Each yaml file represent one match. There are max four innings data  available in each file. Every file contains information about every ball. Along with every ball stats, this file contains following data
* Dates of match days
* Gender(men/women test cricket)
* Match_type(Test/One Day/T20)
* Outcome(Match result)
* Player of the match
* Teams
* Toss winner
* Umpires
* Venue
* Innings

#### Data preparation steps
* Dropped duplicates
* Dropped null values
* Added custom column for boundaries
* Removed outliers
* Corrected team names by using fuzzy matching
* Corrected player names by using fuzzy matching

### Website data: 
  The match is searched on this website by using start date, team1 and team2 from Yaml file. Match Statistics is donwloaded from http://www.howstat.com/ by web scrapping. This data contains statistics for each player for that match and innings totals, etc. The player names are matched by using fuzzy matching as names in Yaml and website have some differences. 

  #### Data preparation steps
  * Fill blank values with appropriate values For Batsman Stats
  * Fill blank values with appropriate values For Bowler Stats
  * Find duplicates for Bowler Stas
  * Replace * and † from Batsman And Dismissal columns
  * Find closest matching player names with Fuzzy matching
  * Corrected Batsman Name
  * Find bowler name from Dismissal column

### API: 
  The player career statistics is donwloaded from http://cricapi.com using API. Player profiles are found in following order
  1. Tried to find player by exact match first
  2. If not found in above step, searched with last-name
  3. Used Fuzzy Matching for name matching if not found with exact match

#### Data preparation steps
  * Correct Profile-Ids as API has some issues with Search functionality
  * Join profile-Ids, batting, and bowling dataframe into one dataframe by using key as Profile-Id
  * Drop duplicate columns
  * Replace ``-'' with pd.np.nan, Intentionally keeping it as NaN to indcate the stats is not applicable for that player
  * Find invalid records or records with all missing values

### Stats and Plots
* Barplot to find typical number innings per match
* Heatmap for Team name fuzzy matching 
* Histogram for batting averages to find outliers
* Histogram for bowling strike rates to find outliers


## Reference:
http://www.howstat.com/

http://cricapi.com
