---
title: "Road Accidents in UK"
date: 2020-06-01
tags:
 - Python
 - Jupyter Notebook
 
excerpt: "EDA of Road Accidents in UK 2010-14"
header:
  overlay_image: "/Projects/Road Accidents in UK/assets/image1.jpeg"
  overlay_filter: 0.3 # same as adding an opacity of 0.3 to a black background
  teaser: "/Projects/Road Accidents in UK/assets/image1.jpeg"
  actions:
    - label: "Go to GitHub Repository"
      url: "https://github.com/sanjayjaras/sanjayjaras.github.io/tree/master/Projects/Road%20Accidents%20in%20UK"
---




# Road Accidents in UK
## EDA of Road Accidents in UK 2010-14

* <h3><p>Introduction</p></h3>

 <p> Accidents data can be used for numerous applications such as real-time accident prediction, studying accident hotspot locations, casualty analysis and extracting cause and effect rules to predict accidents, and studying the impact of vehicle age, road conditions, speed limits, environmental stimuli and road conditions on accident occurrence. This dataset contains the data of road accidents happened in U.K. within the time frame of 2010-2014. The data is very extensive, so it can give many insights on accidents. It contains location information, vehicle information, weather information, driver information, time of accidents etc.</p>
* <h3><p >Research questions</p></h3>
    <font >
    <ol>
      <li>What are the factors those are more correlated to severity of accidents?</li>
      <li>Is vehicle power something to do with accidents?</li>
      <li>Is a particular day of time, when accidents happens more?</li>
      <li>Is number of accidents vary by road types?</li>
      <li>Is accidents increase in winter season ?</li>
    </ol> 
    </font>

* <h3><p >Approach</p></h3>
<p > If required the data will be normalized and cleaned. If null values are present in data, I need to take care of them by either removing those reocrds or using mean value from that column. After cleaning the data, I will analyze data to try answering research questions. While analyzing I will try to use graphs to support/better understand the data.</p>

* <h3><p >Data</p></h3>
<h5><p >Source Link:</p></h5>
<p >https://www.kaggle.com/stefanoleone992/adm-project-road-accidents-in-uk
<h5><p >Columns in the dataset:</p></h5>
 <font >
    <ol>
        <li>Accident_Index: Accident index</li>
        <li>Latitude: Accident latitude</li>
        <li>Longitude: Accident longitude</li>
        <li>Region: Accident region</li>
        <li>Urban_or_Rural_Area: Accident area (rural or urban)</li>
        <li>X1st_Road_Class: Accident road class</li>
        <li>Driver_IMD_Decile: Road IMD Decile</li>
        <li>Speed_limit: Road speed </li>
        <li>Road_Type: Road type</li>
        <li>Road_Surface_Conditions: Road surface condition</li>
        <li>Weather: Weather</li>
        <li>High_Wind: High wind</li>
        <li>Lights: Road lights</li>
        <li>Datetime: Accident datetime</li>
        <li>Year: Accident year</li>
        <li>Season: Accident season</li>
        <li>Month_of_Year: Accident month</li>
        <li>Day_of_Month: Accident day of month</li>
        <li>Day_of_Week: Accident day of week</li>
        <li>Hour_of_Day: Accident hour of day</li>
        <li>Number_of_Vehicles: Accident number of vehicles</li>
        <li>Age_of_Driver: Driver age</li>
        <li>Age_of_Vehicle: Vehicle age</li>
        <li>Junction_Detail: Accident junction detail</li>
        <li>Junction_Location: Accident junction location</li>
        <li>X1st_Point_of_Impact: Vehicle first point of impact</li>
        <li>Driver_Journey_Purpose: Driver journey purpose</li>
        <li>Engine_CC: Vehicle engine power (in CC</li>
        <li>Propulsion_Code: Vehicle propulsion code</li>
        <li>Vehicle_Make: Vehicle make</li>
        <li>Vehicle_Category: Vehicle category</li>
        <li>Vehicle_Manoeuvre: Vehicle manoeuvre</li>
        <li>Accident_Severity: Accident severity</li>
    </ol>
   </font>
<p >This data is from 2010 through 2014. The dataset is very extensive with location information, vehicle information, weather information, driver information, time of accidents.</p>

## References:
https://www.kaggle.com/stefanoleone992/adm-project-road-accidents-in-uk



