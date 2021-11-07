---
title: "Weather Application"
date: 2019-12-01
tags:
 - Python
 - Application
 - Weather
 - API
 - Data Gathering
  
 
excerpt: "Weather application to show weather information by 3 hours for next 5 days by  city name or zipcode"
header:
  overlay_image: "/Projects/Weather Application/assets/image1.jpg"
  overlay_filter: 0.3 # same as adding an opacity of 0.3 to a black background
  teaser: "/Projects/Weather Application/assets/image1.jpg"
  actions:
    - label: "Go to GitHub Repository"
      url: "https://github.com/sanjayjaras/sanjayjaras.github.io/tree/master/Projects/Weather Application"
---




# Weather Application
## Weather application to show weather information by 3 hours for next 5 days by  city name or zipcode

api.openweathermap.org

The application gets weather data for the City/Zipcode from https://api.openweathermap.org/data/2.5/forecast. It can fetch data either by Zipcode or City name. City and zipcode is searched within the selected country(Default selected country is United-StatesUS). For selecting country, we need to provide Country-Code like US or IN. The application will fetch data from openwethermap.org in the form of json. This data is then parsed and displayed in readable format. The weather information is shown for every 3 hours for next 5 days. 

<img src="/Projects/Weather Application/assets/image2.jpg" alt="Menu" />

<img src="/Projects/Weather Application/assets/image3.jpg" alt="Result" />



## Reference:
https://openweathermap.org/api


