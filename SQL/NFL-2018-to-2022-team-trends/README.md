# NFL team stat trends 2018 to 2022
For this project I wanted to analyze all 32 NFL teams' stats from the 2018 season to the 2022 season to see if there were any common trends or stats amongst teams with winning and losing records. The data used for this analysis came from Kaggle's [NFL Team Stats 2002 - Feb. 2023 (ESPN)](https://www.kaggle.com/datasets/cviaxmiwnptr/nfl-team-stats-20022019-espn) dataset. I chose to only use the 
2018-2019 to 2022-2023 seasons because there were a few games missing from earlier seasons and the data sample size was sufficient enough for this analysis.

# Technologies Used

- [Google Cloud Big Query](https://cloud.google.com/bigquery?hl=en) - A SQL, cloud data-warehouse in Google Cloud Platform
- [Google Sheets](https://www.google.com/sheets/about/) - A web-based spreadsheet application in the Google Docs Editor Suite


# Step 1.
The first step was identifying the problem(s) or question(s) that needed to be answered with this analysis. The questions were:
  - Who are the most winningest and losing teams in the NFL?
  - What stats are common among the aforementioned teams? 

# Step 2.
The second step was figuring out what data was needed for this analysis, as I wanted to gather quantitative team data so that the stats aren't biased based off of star players on teams. So, I did some research and found the [NFL Team Stats 2002 - Feb. 2023 (ESPN)](https://www.kaggle.com/datasets/cviaxmiwnptr/nfl-team-stats-20022019-espn) dataset on Kaggle.  The data was then cleaned in Google Sheets, stored as .csv file and then imported into Google Cloud BiqQuery for further analysis. 

# Step 3.
The third step involved cleaning and manipulating the data to get the stats needed for the analysis. I started this step by importing the data into Google Sheets and analyzing what columns were needed for the calculations. I then removed rows that had a date before 09/01/2018 to get the relevant rows for the sample. Next, I used the RIGHT() function to transform the string values into two integers. The following stats are in the format:
  
  orig_stat - > new_stat_1 & new_stat_2
  - third_downs_away -> third_downs_converted_away & third_downs_attempted_away
  - third_downs_home -> third_downs_converted_home & third_downs_attempted_home
  - fourth_downs_away -> fourth_downs_converted_away & fourth_downs_attempted_away
  - fourth_downs_home -> fourth_downs_converted_home & fourth_downs_attempted_home
  - comp_att_away -> pass_completions_away & pass_attempts_away
  - comp_att_home -> pass_completions_home & pass_attempts_home
  - sacks_away -> sacks_allowed_away & sacks_yards_lost_away
  - sacks_home -> sacks_allowed_home & sacks_yards_lost_home
  - penalties_away -> penalties_away & penalty_yards_away
  - penalties_home -> penalties_home & penalty_yards_home
  - redzone_away -> redzone_conversions_away & redzone_trips_away
  - redzone_home -> redzone_conversions_home & redzone_trips_home

Below are a couple of screenshots showing the dirty and clean data.

Dirty data:
![original-stats-screenshot ](https://github.com/ShaunJPartridge/Data-Analytics-Portfolio/assets/47838616/628744dd-b33d-437e-9e6b-b18b3466bbd6)
Clean data:
![cleaned-stats-creenshot](https://github.com/ShaunJPartridge/Data-Analytics-Portfolio/assets/47838616/0799ae65-8b5a-4439-a109-ac77eb309a8b)


The following were the rest of the stats used for this analysis:
  - away & home
  - score_away & score_home
  - passing_yards_away
  - passing_yards_home
  - rushing_yards_away & rushing_attempts_away
  - rushing_yards_home & rushing_attempts_home
  - def_st_td_away & turnovers_away
  - def_st_td_home & turnovers_home


# Step 4.
Now that the data is cleaned, we are going to import the .csv file into Google Cloud BigQuery and use SQL to perform calculations and generate a new spreadsheet
containing the following computed stats for each season:
  - team
  - yr_record
  - yr_3rd_down%
  - yr_4th_down%
  - yr_ypc (yards per catch)
  - yr_ypr (yard per rush)
  - yr_rz% (red zone percentage)
  - yr_ypp (yards per penalty)
  - yr_dst_points (defense/special teams points)
  - yr_turnovers

A CTE and aggregation functions we're used to gather the stats above. The CTE, getSums, involved combining a home and away table by UNIONing the stats that we're generated in step three, for each team when they were the away and home team, and then using the SUM function to accumulate each stat for each team. The CTE is grouped by team and ordered by date. The date column is selected so that the stats can be queried by the date in the next query. Below is the CTE.

![getSums-SS1](https://github.com/ShaunJPartridge/Data-Analytics-Portfolio/assets/47838616/1b7d4281-524d-49c9-a602-dc4cff93676b)
![getSums-SS2](https://github.com/ShaunJPartridge/Data-Analytics-Portfolio/assets/47838616/7b4d786c-e056-43f3-96e8-73c9a7fd5a31)

The next and final query was used to get teams' name, along with their record and stats for each season from 2018 to 2022. The seasons were gathered by JOINing 5 tables, each representing a season, on the name column. Each stat returned respresents the average for that particular stat in every season. Each season 
is collected by using the date column in the WHERE clause of each subquery. The final table is ordered by teams' total wins over the last 5 seasons in descending order. The query can be referenced below.

![final-query-1-ss](https://github.com/ShaunJPartridge/Data-Analytics-Portfolio/assets/47838616/190a8255-5024-4ed9-9bdc-2f34805c037f)
![final-query-2-ss](https://github.com/ShaunJPartridge/Data-Analytics-Portfolio/assets/47838616/0c0e62e7-7465-4d65-bc99-21dfcdd6d4ea)
![final-query-3-ss](https://github.com/ShaunJPartridge/Data-Analytics-Portfolio/assets/47838616/a7d93b3b-2a35-479e-91ee-d60d94718d0c)
![final-query-ss-4](https://github.com/ShaunJPartridge/Data-Analytics-Portfolio/assets/47838616/d715aa94-031d-424e-a2bf-d6a981d8b60c)






To view the complete SQL script in Google Cloud BigQuery, click [here](https://console.cloud.google.com/bigquery?sq=129548345512:86c4bff89dd0408da67dd4211b61c7d3).

# Step 5.
The results from the query above will now be exported to Google Sheets so that they can be shared in a more concise manner. A new tab was created in the spreadsheet to show the most winningest teams', highlighted in bright blue, and the rest of the leagues' (ROL) stat averages over the past five seasons. Conditional formatting was used to visualize the averages for each team, as well as compare the averages of the most winningest teams to the ROL. The AVERAGE function was used in the new tab to get the averages of each stat for each team using data from the imported spreadsheet, NFL_TEAM_STATS_2018_TO_2022, from Google BigQuery. The parameters passed in the function are the following:
  - NFL_TEAM_STATS_2018_TO_2022!C2: this represents the stat for a paricular team in the 2018 season
  - NFL_TEAM_STATS_2018_TO_2022!L2: this represents the stat for the same team in the 2019 season
  - NFL_TEAM_STATS_2018_TO_2022!U2: this represents the stat for the same team in the 2020 season
  - NFL_TEAM_STATS_2018_TO_2022!AD2: this represents the stat for the same team in the 2021 season
  - NFL_TEAM_STATS_2018_TO_2022!AM2: this represents the stat for the same team in the 2022 season

Each stat column represents the range of data that the conditional formatting was used on, where each cell's color corresponds with the value inside of it. For example, the lesser the value in a cell the lighter its shade and vice-versa. The spreadsheet can be referenced below.

![team-avgs-ss-1](https://github.com/ShaunJPartridge/Data-Analytics-Portfolio/assets/47838616/d286b5b0-1245-49e2-bf7e-c818b21271ad)
![team-avgs-ss-2](https://github.com/ShaunJPartridge/Data-Analytics-Portfolio/assets/47838616/c6b5b835-bb4d-4edb-acf1-314cd0995282)

Next, a 9x3 table with conditional formatting was created to compare the top 13 most winningest teams and the ROL' stat averages over the past five seasons. Thirteen teams were used instead of ten because two teams were tied at 3rd place and three teams were tied at 9th place. The table can be reference below.

![avg-table-ss](https://github.com/ShaunJPartridge/Data-Analytics-Portfolio/assets/47838616/55e5d8c1-c08c-4099-833c-d736aa94445f)

From the table above, the few stats that have a significant difference are 3rd and 4th down conversion percentage, redzone conversion percentage, and defense/special teams points. It's clear that the top 13 teams convert on more crucial downs to extend drives, as well as turn their drives into points near the goal line and score with their defense and special teams.

To view the complete Google Sheet, click [here](https://docs.google.com/spreadsheets/d/1_EnJwNf1L5uvE38vvAfg1oJl_iUcfAlO9dWKNdUHeq0/edit?usp=sharing)

# Step 6
The ideal stakeholders for this analysis would be team owners, GMs, scouts, and coaches. They could use this analysis to evaluate their own teams and decide what side(s) of the ball need improvement. Improvement can be accomplished by drafting players in key positions, trading for a player or players during the season, or signing free agents who could also help their team.

