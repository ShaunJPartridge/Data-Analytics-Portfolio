# NFL team stat trends 2018 to 2022
For this project I wanted to analyze all 32 NFL teams' stats from the 2018 season to the 2022 season to see if there were any common trends amongst teams that have double digit wins compared to teams with single digit wins. The data used for this analysis came from Kaggle's [NFL Team Stats 2002 - Feb. 2023 (ESPN)](https://www.kaggle.com/datasets/cviaxmiwnptr/nfl-team-stats-20022019-espn) dataset. I chose to only use the 
2018-2019 to 2022-2023 seasons because there were a few games missing from earlier seasons and the data sample size was sufficient enough for the analysis.

# Technologies Used

- [Google Cloud Big Query](https://cloud.google.com/bigquery?hl=en) - A SQL, cloud data-warehouse in Google Cloud Platform
- [Google Sheets](https://www.google.com/sheets/about/) - A web-based spreadsheet application in the Google Docs Editor Suite


# Step 1.
The first step was identifying the problem or question that needed to be answered with this analysis. The question was:
  - What stats are common among the most winningest teams in the NFL?

# Step 2.
The second step involved figuring out what data was needed for this analysis. So, I did some research and found the [NFL Team Stats 2002 - Feb. 2023 (ESPN)](https://www.kaggle.com/datasets/cviaxmiwnptr/nfl-team-stats-20022019-espn) dataset on Kaggle. The data was then cleaned and stored as .csv and imported into Google Cloud BiqQuery for further analysis. 

# Step 3.
The third step involved cleaning and manipulating the data to get the needed stats for analysis. I started this step by importing the data into Google Sheets and analyzing what columns
needed to be manipulated to perform ca.

This is the result of the data cleaning process
The stats used from the dataset are the following:
  - away & home
  - score_away & score_home
  - third_downs_converted_away & third_downs_attempted_away
  - third_downs_converted_home & third_downs_attempted_home
  - fourth_downs_converted_away & fourth_downs_attempted_away
  - fourth_downs_converted_home & fourth_downs_attempted_home
  - passing_yards_away & pass_completions_away
  - passing_yards_home & pass_completions_home
  - rushing_yards_away & rushing_attempts_away
  - rushing_yards_home & rushing_attempts_home
  - redzone_conversions_away & redzone_trips_away
  - redzone_conversions_home & redzone_trips_home
  - penalty_yards_away & penalties_away
  - penalty_yards_home & penalties_home
  - def_st_td_away & turnovers_away
  - def_st_td_home & turnovers_home
The data gathered from Kaggle was then cleaned and stored as .csv and imported into Google Cloud BiqQuery for further analysis.
    


