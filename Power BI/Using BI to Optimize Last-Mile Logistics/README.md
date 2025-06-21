# Using BI to Optimize Last-Mile Logistics

## Data Analysis Process

### 1. Define the Problem
Amazon has noticed a decline in delivery performance, with customers experiencing delays in receiving their packages. To investigate the root causes, I analyzed over 30,000 delivery records to uncover insights that can help improve efficiency and optimize operations. This analysis explores customer behavior, delivery performance, product trends, and traffic impacts—both overall and across different service areas.

**Guiding Questions**:

   - What factors affect delivery efficiency?  
   - Which product categories are most and least popular?  
   - How do traffic, delivery area, and vehicle type impact transit time?  
   - When are orders most frequently placed?  
   - What patterns exist in agent performance across different conditions?  

### 2. Collect the Data


**Dataset Source**:

The dataset used for this analysis was downloaded from Kaggle and can be found at [Amazon Delivery Dataset](https://www.kaggle.com/datasets/sujalsuthar/amazon-delivery-dataset)

**Key Features**:

**Size**: 43,648 rows x 16 columns

**Features**:

 - `Order_ID`
 - `Agent_Age` (numeric)
 - `Agent_Rating` (decimal)
 - `Transit_Time` (in minutes)
 - `Traffic`, `Weather`, `Vehicle` (categorical)
 - `Area`, `Order_Date`, `Category`

<img src="pics/amazon-data-all-cols.png">


### 3. Clean & Prepare the Data

**Data Cleaning Tasks**:

   - Removed invalid geolocation values (`Store_Latitude`/`Store_Longitude` = 0 - in the Indian Ocean)

   |![](pics/store-lat-col-dirty.png)|![](pics/store-lat-col-clean.png)|
   |:-:|:-:|
   |Before|After|
  
   - Dropped rows with a blank in the `Transit_Time` column to preserve metric integrity 

   ![](pics/power-query-removing-blank-transit-col.png)

   - Standardized data types (e.g., converted agent age from string to integer)
   
   - Capitalized first letter of `Vehicle` types for better visuals

**Feature Engineering**:

   - Created `Month`, `Weekday`, `Weekday_Name` columns using Power Query date functions

   |![](pics/power-query-month-col.png)|![](pics/power-query-weekday-col.png)|![](pics/power-query-day-name-col.png)|
   |:-:|:-:|:-:|

   - Built `Time_of_Day` column using DAX SWITCH() for Morning/Afternoon/Evening/Night

   - Created `Amount_Of_Orders` measure to track volume

   |![](pics/DAX-time-of-day.png)|![](pics/DAX-count-of-orders.png)|
   |:-:|:-:|

   - Ensured bar chart would be sorted by `Weekday_Name` using numerical `Weekday` values

   <img src="pics/sort-by-week-day-name.png" style="width:400px; height:400px;">
   

### 4. Analyze the Data

**a. Time-Series Trends**:

   - Significant order increases from Feb 18 – Mar 1 (likely due to end-of-month promotions)

   - March had the most complete data; February and April had partial coverage

   - Delivery times varied significantly based on traffic and area:  

     * Fastest: low-traffic urban areas  

     * Slowest: semi-urban in high traffic

**b. Traffic Pattern Insights**:

   - Traffic Jams = longest average transit times (148 mins), lowest ratings

   - Low traffic = quickest deliveries (101 mins), highest ratings

**c. Descriptive & Exploratory Analysis**:

   - Majority of deliveries were made to Metropolitan areas (30K+ orders)

   - Motorcycles were the most used delivery vehicle across all areas

   - Evenings had the highest order activity, especially on Wednesdays and Sundays

   - Electronics, books, and jewelry were the top products purchased


### 5. Share & Visualize Results

**4.a Time-Series Trends Visuals**:

   |![](pics/home-db-all.png)|![](pics/home-db-urban-low-fastest-avg-time.png)|
   |:-:|:-:|
   |![](pics/home-db-semi-urban-high-lowest-avg-time.png)|![](pics/home-db-all-traffic-other-area.png)|
   
**4.b Traffic Pattern Insights Visuals**:

   |![](pics/home-db-traffic-jam-all-areas.png)|![](pics/home-db-low-traffic-all-areas.png)|
   |:-:|:-:|

**4.c Descriptive & Exploratory Analysis Visuals**:

   |![](pics/cats-db.png)|![](pics/cats-db-feb.png)|
   |:-:|:-:|
   |![](pics/cats-db-march.png)|![](pics/cats-db-april.png)|


### 6. Act (Draw Conclusions & Recommend Actions)

### Key Takeaways:

   - Transit time influences agent ratings — the quicker the delivery, the better the customer feedback

   - Agents riding motorcycles in low traffic, urban areas are the fastest and get the highest ratings

   - Delivery optimization should prioritize time of day, vehicle type, and regional traffic trends

   - High traffic times correlate with Afternoon deliveries that consist mostly of skincare, sports, and pet supplies products

   - Evening orders dominate—especially on Wednesdays and Sundays

### Strategic Recommendations:

   - Route deliveries to Urban/Other zones during low-traffic times

   - Assign motorcycle deliveries for congested routes

   - Focus on high-efficiency time slots (Evenings, Weds/Thurs) to deliver packages

   - Use agent performance data for training purposes

   - Develop demand-based staffing forecasts by day & hour
