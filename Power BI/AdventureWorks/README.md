# Adventure Works Data Analysis

This data analysis involved tracking KPI's, compare regional performance, analyze product-level trends, and identify high-level customers for Adventure Works, a global manufacturing company that produces cycling equipment and accesories. The data used for this analyis was a folder of raw csv files containing information about transactions, returns, products, customers, and sales territories between 1/1/2020 and 6/1/2022.

# Technologies Used
 - [Microsoft Power BI](https://www.microsoft.com/en-us/power-platform/products/power-bi)

# Ask
The first step was identifying the problem(s) or question(s) that needed to be answered with this analysis. The questions were:

 - How is the company performing monthly and overall?
 - How close are the goals for monthly revenue, orders, and return rate?
 - What are the metrics for each product category?
 - Are the revenue goals being achieved each month?
 - What are the top 10 products?
 - Who are the top customers?
 - What are the most ordered and returned items? 
 - What country had the most orders?
 - What income levels and occupations made the most purchases?


# Prepare
The second step was organizing and structuring the data from multiple files using data models. Three were made to create relationships between the fact and dimensional tables, allowing for efficient analysis and insighful visualizations by establishing clear connections between different data points. The metrics that will be used throughout this analysis and help answer the questions above are: revenue, profit, total orders, and return rate. To visualize these metrics, KPI's and charts will be used to track the company's performance and cards and tables will display category visualizations.

# Process 
The third step involved cleaning and manipulating the data using M code in the Power Query Editor and DAX in table view. In the Power Query Editor, the first step was to create column headers by promoting the first row of data in each table. After making column headers, some of the columns were either deleted or have data types manipulated so that the data could be more intuitive as well as easier to use for calculations. The following steps were created to make new calculated columns using M code's Date/Time functions:
 - Day Name
 - Start of Week, Month, and Quarter
 - Month and Month Name
 - Start of Year and Year

In table view, columns were formatted intuitvely to the data they contained, such as those containing currency as strings and changing it to a decimal or whole number. DAX function were used to create the following calculated columns:
 - Customer Full Name
 - Income Level
 - Customer Priority
 - Education Category

# Analyze


# Share


# Act
