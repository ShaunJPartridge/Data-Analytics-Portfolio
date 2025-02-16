# Adventure Works Data Analysis

This data analysis involved tracking KPI's, compare regional performance, analyze product-level trends, and identify high-level customers for Adventure Works, a global manufacturing company that produces cycling equipment and accessories. The data used for this analyis was a folder of raw csv files containing information about transactions, returns, products, customers, and sales territories between 1/1/2020 and 6/1/2022.

# Technologies Used
 - [Microsoft Power BI](https://www.microsoft.com/en-us/power-platform/products/power-bi)

# Ask
The first step was identifying stakeholders' problem(s) or question(s) that needed to be answered with this analysis. The questions were:

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
The second step was organizing and structuring the data from multiple files using data models. Three were made to create relationships between the fact and dimensional tables, allowing for efficient analysis and insighful visualizations by establishing clear connections between different data points. The metrics that will be used throughout this analysis and help answer the questions above are: revenue, profit, total orders, and return rate. To help visualize these metrics, KPI's and charts will be used to track the company's performance and cards and tables will display category visualizations.

# Process 
The third step involved cleaning and manipulating the data using M code in the Power Query Editor and DAX in table view. In the Power Query Editor, the first step was to create column headers by promoting the first row of data in each table. After making column headers, some of the columns were either deleted or have data types manipulated so that the data could be more intuitive as well as easier to use for calculations. The following steps were created to make new calculated columns using M code's Date/Time functions:
 - Day Name
 - Start of Week, Month, and Quarter
 - Month and Month Name
 - Start of Year and Year

In table view, columns were formatted intuitvely to the data they contained, such as those containing currency as strings and changing it to either a decimal or whole number. DAX function were also used to create the following calculated columns:
 - Customer Full Name
 - Income Level
 - Customer Priority
 - Education Category

# Analyze
After cleaning the data, several DAX measures were created in report view to help build the dashboards. The following are some of the key measures used:

 - Total Revenue, Total Orders, Return Rate, Total Profit
 - Previous Month Revenue, Orders, and Returns
 - Total Customers, Avg Revenue Per Customer, Total Orders (Customer Detail), Total Revenue (Customer Detail)

The measure table below was created to keep all of the measures in one location for organizational purposes. 

![Screenshot 2025-02-16 103001](https://github.com/user-attachments/assets/dcf41152-317b-4e98-beb7-cfb352fb0081)


The Total Orders and Revenue (Customer Detail) columns are blank because they are displayed using a table with filters and a page filter as seen below. 

![Screenshot 2025-02-15 191506](https://github.com/user-attachments/assets/4dc79311-741f-45b8-9b00-f549ff111b71)

# Share
After creating the measures, three filtered dashboards were used to visualize them and show stakeholders KPI's and key metrics. The first was a top-level dashboard used for executive stakeholders such as the CEO, COO, and VP, to show the company's overall performance. Total profit, returns, revenue, orders, and orders by category were illustrated in the dashboard below using cards and a bar graph.

![AW-EXEC-DB](https://github.com/user-attachments/assets/bcea88ba-a7c7-4bd2-8d4d-200d332dffa1)

Revenue and returns goals were achieved and can be seen in the KPI cards, along with a line chart to show a positive monthly revenue trend between 1/1/2020 and 6/1/2022. 

![AW-EXEC-DB-WITH-TOOLTIP](https://github.com/user-attachments/assets/0365f96b-cffc-48a8-a4c8-4721d88784eb)


The top 10 performing products were visualized in a table. However, this table shows the top 10 products based on either revenue, orders, or return rate. The most ordered and returned item were displayed in cards with the Top N filters.

<table>
 <tr>
  <td><img src="https://github.com/user-attachments/assets/94f18dfa-9a7d-4890-a36f-1b79faf92ff3" width="300" height="200"></td>
  <td><img src="https://github.com/user-attachments/assets/ada077cc-c767-410a-b018-45929603101f" width="300" height="200"></td>
  <td><img src="https://github.com/user-attachments/assets/e7ef1e9e-ab46-4bac-bca4-a791d73e2ec5" width="300" height="200"></td>
 </tr>
</table>

Since Adventure Works is a global company, a map dashboard was used to illustrate the proportion of orders in each country they have customers in. 

![image](https://github.com/user-attachments/assets/14f07a8a-0d72-4dff-9c2c-70bb5d96ab85)


It is apparent that North America, the United States in particular, placed the most orders, followed by Europe, and then Australia.

To get a closer look at these orders, a customer dashboard with two views was used to capture more insights at customer purchasing trends and metrics. The orders by income level and occupation metrics indicate that professionals with an average income made the most purchases. Professionals, on average, also generate almost $200 more in revenue than customers in other any occupations. It's also worth noting that customers in a management role or have a high income made the least amount of purchases.


![image](https://github.com/user-attachments/assets/cc35f607-127f-4461-8220-6a5d607ae3e9)

The top customer by revenue overall was Mr. Maurice Shan but between 2021 and 2021 it was Mr. Larry Vazquez. The top 100 customers were also sorted by revenue generated over orders placed. 

<table>
 <tr>
  <td><img src="https://github.com/user-attachments/assets/b6b24c83-19b4-4dbc-93d4-835e7aab4778" width="450" height="250"></td>
  <td><img src="https://github.com/user-attachments/assets/8320036d-6a77-4187-9eb4-561ad3a7b541" width="450" height="250"></td>
 </tr>
</table>

Another interesting observation was that as the amount of customers increased over time, the revenue generated per customer decreased. This drastic change can be seen with the line chart in the Total Customers and Revenue Per Customer views.

<table>
 <tr>
  <td><img src="https://github.com/user-attachments/assets/a6c6239f-47c0-4c49-8844-806f0a6d2a57" width="450" height="250"></td>
  <td><img src="https://github.com/user-attachments/assets/3e57cb18-afa2-441f-81c1-51d3d3243bcc" width="450" height="250"></td>
 </tr>
</table>


# Act
