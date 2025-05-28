# Telecom Customer Churn Analysis

## Data Analysis Process

### 1. Define the Problem

Telecom Co., a US-based telecommunications company that offers national and international phone services, is experiencing a high volume of customers canceling their phone service, which is costing the company thousands of dollars in losses.

**Identify Business Goal:**
To solve this, I'm proposing a proactive solution to predict at-risk customers using Logistic Regression and Gradient Boosted Tree machine learning models and take action to prevent them from churning.

### 2. Collect & Store Data

The dataset will be scraped from an online source, Kaggle, and cleaned using a Python script.

In this script:

Kaggle's API and pandas are used to authenticate the connection, extract the .csv file from the repository, and read it into a pandas DataFrame.

It is then transformed back into a .csv file for the blob used to write to the GCS bucket.

An instance of GCP's Storage client is initialized to gain access to the GCS bucket and upload the data.

Once uploaded, an external BigQuery table is created by retrieving the dataset from the GCS bucket.

This table serves as a reference to create/update the final churn-features table, which is used to train the ML models and analyze in Power BI. In BigQuery, scheduled queries train the models and store results in native tables. Only the predictions from the most accurate model are analyzed in Power BI.

Insert DFD screenshot here.

### 3. Clean & Prepare Data

Use Kaggle API and pandas to read in the dataset, and SQL to transform values, normalize features, and engineer churn indicators (total_minutes, total_charges, total_calls, vm_plan, int_plan, tier).

**Data Cleaning & Transformations:**

Columns international_plan, voice_mail_plan, and churn are cast from boolean to INT64 for the ML model.

The function get_query_string does 90% of the transformation work.

The getTotals CTE aggregates totals using SAFE_CAST and TRUNC to ensure precision.

Trailing white spaces in customer_id are removed.

international_plan and voice_mail_plan are transformed for better readability in dashboard slicers.

Insert get_query_string function screenshot here.
Insert create query function screenshot here.

Remaining transformations are handled in scheduled BigQuery queries.

**Modeling:**

Logistic Regression was chosen for its simplicity and scalability but only achieved 77.48% accuracy.

Gradient Boosted Trees achieved 96.68% accuracy and was chosen as the final model.

Customers are segmented by churn probability into tiers:

**Low-Risk:** 0 - 0.40 (non-inclusive)

**Medium-Risk:** 0.40 - 0.70 (non-inclusive)

**High-Risk:** 0.70 - 1.00 (non-inclusive)

Insert model prediction queries and results screenshots here.

Power BI connects to BigQuery using Direct Query for real-time analysis.

### 4. Analyze & Visualize

Explore data distributions, correlations, and trends using visualizations to identify key churn drivers.

A star-schema data model was used to ensure filters apply correctly across visuals. Insights are organized by sections below.

**Service Usage by Risk Tier**

**Risk Tier**

**Total Charges**

**Total Calls**

**Total Minutes**

Low-Risk

$217,470.00

1,132,727

2,172,621.66

High-Risk

$28,923.83

128,265

277,934.72

Medium-Risk

$6,261.92

32,494

62,101.01

Insert screenshot here.

**Churn Insights by Plan Type and Risk Tier**

**Overall Population:**

Total customers churned: 598

Overall churn rate: 14.07%

Revenue lost from churn: $39.19k

**Churn by Risk Tier:**

Low-Risk: 3,720 customers; 2.74% churn rate

Medium-Risk: 106 customers; 69.81% churn rate

High-Risk: 424 customers; 99.53% churn rate

**State Insights:**

New Jersey had the highest churn rate at 27.08%

Insert screenshot here.

Continue inserting screenshots and detailed breakdowns for all plan type segments.

### Key Takeaways

High-Risk customers consistently churn at rates near or at 100%, especially those with international plans.

Voicemail plans are linked to lower churn rates, especially among Low and Medium-Risk groups.

International plans are a strong churn predictor with over 42% churn.

New Jersey frequently appears with the highest churn rate.

### Strategic Recommendations

**Prioritize Retention for Medium and High-Risk Segments**

Focus on targeted outreach: retention offers, proactive support, loyalty rewards.

**Enhance International Plan Offerings**

Bundle voicemail services or offer discounts for combined plans.

**Focus on At-Risk States**

Target retention in New Jersey, Maine, New Hampshire. Investigate service or perception issues.

**Drive Engagement in Low-Usage Segments**

Use personalized comms, onboarding support, and usage incentives.

### 5. Deploy & Monitor

BigQuery's built-in ML models and scheduler are used for automation.

Training queries run every Monday at 9:00 AM EST.

Export queries run at 10:00 AM EST.

Power BI reflects updates post-10:00 AM. Scheduling ends September 1, 2025, due to cloud budget limits.