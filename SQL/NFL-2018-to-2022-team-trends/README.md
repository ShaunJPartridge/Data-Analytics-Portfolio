# NFL team stat trends 2018 to 2022
For this project I wanted to analyze all 32 NFL teams' stats from the 2018 season to the 2022 season to see if there were any common trends amongst teams that have double digit wins compared to teams with single digit wins. The data used for this analysis came from Kaggle's [NFL Team Stats 2002 - Feb. 2023 (ESPN)](https://www.kaggle.com/datasets/cviaxmiwnptr/nfl-team-stats-20022019-espn) dataset. I chose to only use the 
2018-2019 to 2022-2023 seasons because there were a few games missing from earlier seasons and the data sample size was sufficient enough for this analysis.

# Technologies Used

- [Google Cloud Big Query](https://cloud.google.com/bigquery?hl=en) - A SQL, cloud data-warehouse in Google Cloud Platform
- [Google Sheets](https://www.google.com/sheets/about/) - A web-based spreadsheet application in the Google Docs Editor Suite


# Step 1.
The first step was identifying the problem or question that needed to be answered with this analysis. The question was:
  - What stats are common among the most winningest teams in the NFL?

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


The following were the rest of the stats needed for this analysis:
  - away & home
  - score_away & score_home
  - passing_yards_away
  - passing_yards_home
  - rushing_yards_away & rushing_attempts_away
  - rushing_yards_home & rushing_attempts_home
  - def_st_td_away & turnovers_away
  - def_st_td_home & turnovers_home


The cleaned data was then stored as .csv file and imported into Google Cloud BiqQuery for further analysis.

# Step 4.
    


