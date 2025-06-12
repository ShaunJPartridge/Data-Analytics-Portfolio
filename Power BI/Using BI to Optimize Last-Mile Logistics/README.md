# Using BI to Optimize Last-Mile Logistics

# Objective:
This project explores a large dataset of Amazon deliveries to uncover insights that can improve delivery efficiency and optimize operations. The analysis focuses on customer behavior, delivery performance, product trends, and traffic impacts—both overall and by area.

# 1. Ask the Right Questions (Define the Problem)

## Guiding Questions:

   - What factors affect delivery efficiency?  
   - Which product categories are most and least popular?  
   - How do traffic, delivery area, and vehicle type impact transit time?  
   - When are orders most frequently placed?  
   - What patterns exist in agent performance across different conditions?  

# 2. Collect the Data

## Dataset Source:

The dataset used for this analysis was downloaded from Kaggle and can be found at [Amazon Delivery Dataset](https://www.kaggle.com/datasets/sujalsuthar/amazon-delivery-dataset)

## Key Features:

**Size**: 43,648 rows x 16 columns

**Features**:

 - Agent Age (numeric)
 - Agent Rating (decimal)
 - Delivery Time (in minutes)
 - Traffic, Weather, Vehicle (categorical)
 - Area, Order Date, Category

<img src="pics/amazon-data-all-cols.png">

# 3. Clean & Prepare the Data

## Data Cleaning Tasks:

   - Removed invalid geolocation values (e.g., stores lat/lon = 0 - in the Indian Ocean)

   |![](pics/store-lat-col-dirty.png)|![](pics/store-lat-col-clean.png)|
   |:-:|:-:|
   |Before|After|

   - Dropped rows with blank transit times to preserve metric integrity 

   ![](pics/power-query-removing-blank-transit-col.png)

   - Standardized data types (e.g., converted agent age from string to integer)
   
   - Capitalized first letter of vehicle types for better visuals


## Feature Engineering:

   - Created Month, Weekday, Weekday Name using Power Query date functions

   |![](pics/power-query-month-col.png)|![](pics/power-query-weekday-col.png)|![](pics/power-query-day-name-col.png)|
   |:-:|:-:|:-:|

   - Built Time_of_Day column using DAX SWITCH() for Morning/Afternoon/Evening/Night

   - Created Amount_Of_Orders measure to track volume

   |![](pics/DAX-time-of-day.png)|![](pics/DAX-count-of-orders.png)|
   |:-:|:-:|

   - Ensured weekday sorting using numerical weekday values

   <img src="pics/sort-by-week-day-name.png" style="width:400px; height:400px;">

# 4. Analyze the Data

## Descriptive & Exploratory Analysis:

   - Majority of deliveries made to Metropolitan areas (30K+ orders)

   - Motorcycles were the most used delivery vehicle across all areas

   <img src="pics/cats-del-in-area-per-vehicle.png" style="width:400px; height:400px;">

   - Evening had the highest order activity, especially Wednesdays and Sundays

   - Electronics, books, and jewelry were top products

## Time-Series Trends:

    Significant order increases from Feb 18 – Mar 1 (likely due to end-of-month promotions)

    March had the most complete data; February and April had partial coverage

    Delivery times varied significantly based on traffic and area:

        Fastest transit times: low-traffic urban zones

        Slowest: semi-urban in high traffic

## Traffic Pattern Insights:

    Jammed traffic = longest average transit times (148 mins), lowest ratings

    Low traffic = quickest deliveries (101 mins), highest ratings

    Semi-urban = fewest orders, longest transit times, lowest agent ratings

# 5. Share & Visualize Results

## Dashboard Features:

    Multi-filtered views (by area, traffic, time of day, etc.)

    KPIs for agent ratings, transit times, order volumes

    Charts for order frequency by weekday, time of day, and product category

    Scaled Y-axis for Avg Transit Time Throughout the Week for consistent interpretation

# 6. Act (Draw Conclusions & Recommend Actions)

## Key Takeaways:

    Optimize routing based on area, traffic, and time of day

    Promote motorcycle usage for congested zones

    Use delivery trends to better forecast demand and staffing needs

    Evening hours (esp. Wednesdays/Thursdays) offer high delivery efficiency

    Monitor agent ratings as a proxy for customer satisfaction and delivery time

    Improve semi-urban logistics by possibly expanding warehouse coverage
