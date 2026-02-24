# 🛒 Retail Performance Analytics Dashboard  
### Excel Data Model | Power Pivot | DAX | Time-Series Forecasting

---

## 📌 Executive Summary

This project presents an interactive **Retail Performance Analytics Dashboard** built using Microsoft Excel’s Data Model and DAX.

The objective was to simulate a real-world retail analytics scenario (similar to Coles/Woolworths operations) and design a decision-support tool that enables business leaders to monitor revenue performance, profitability, operational efficiency, and short-term revenue outlook.

The dashboard transforms raw transactional sales data into structured business intelligence insights with interactive filtering and predictive forecasting.

---

## 🎯 Business Objectives

Retail decision-makers need visibility into:

- Which product categories drive the highest revenue?
- Which categories generate the strongest profit margins?
- Where is operational leakage occurring (wastage)?
- Which stores outperform others?
- Are there seasonal patterns in revenue?
- What is the projected revenue for the next quarter?

This dashboard was designed to answer these questions in a clear, executive-ready format.

---

## 🛠 Tools & Technologies Used

- Microsoft Excel
- Excel Data Model (Relational Modeling)
- Power Pivot
- DAX (Data Analysis Expressions)
- Pivot Tables & Pivot Charts
- Slicers for interactivity
- Excel ETS Time-Series Forecasting Model

---

## 🧱 Data Model Architecture

The solution uses a structured relational model:

- **Sales Table** (Transactional revenue data)
- **Products Table** (Category and cost structure)
- **Stores Table** (Store-level metadata)
- **Calendar Table** (Time dimension)
- **Inventory Table** (Operational metrics)

Relationships were established using `Product_ID`, `Store_ID`, and `Date` keys to enable accurate aggregation and filtering.

---

## 📊 Dashboard Components

### 🔹 KPI Layer

- Total Revenue  
- Gross Profit  
- Gross Margin %  
- Inventory Turnover  
- Wastage Cost  

All KPIs were calculated using DAX measures to ensure correct aggregation logic under dynamic filtering.

---

### 🔹 Category-Level Analysis

- Revenue by Category  
- Gross Margin % by Category  
- Wastage Cost by Category  

This enables comparison of scale vs profitability vs operational efficiency.

---

### 🔹 Trend Analysis

- Monthly Revenue Trend (2024)  
- Identification of seasonal patterns  

The dashboard highlights December revenue surge and post-seasonal normalization.

---

### 🔹 Store Performance Analysis

- Top Performing Stores by Revenue  
- Interactive store filtering  

Allows management to benchmark performance across locations.

---

### 🔹 Predictive Analytics Layer

- 3-Month Revenue Forecast (Jan–Mar 2025)  
- Implemented using Excel’s ETS model  
- Includes confidence interval bands  

This extends the dashboard from descriptive analytics to predictive planning.

---

## 🧠 Key Insights Generated

- Pantry category drives the highest revenue contribution.  
- Bakery delivers the strongest gross margin (~30%).  
- Produce category shows the highest wastage cost, indicating operational inefficiency.  
- Revenue peaks in December, followed by expected seasonal correction.  
- Q1 2025 revenue forecast projects stabilization within confidence bounds.

---

## 📈 Analytical Approach

1. Built relational data model inside Excel.  
2. Created DAX measures for:
   - Total Revenue  
   - Gross Profit  
   - Margin %  
   - Turnover  
   - Wastage Cost  
3. Designed interactive pivot-based visualizations.  
4. Implemented slicers for dynamic filtering.  
5. Applied time-series forecasting using ETS model.  
6. Interpreted results from a business strategy perspective.

---

## 💡 What This Project Demonstrates

- Strong understanding of data modeling concepts  
- Ability to write and apply DAX measures  
- Designing executive-ready dashboards  
- Translating data into actionable business insight  
- Applying time-series forecasting in Excel  
- Business-oriented analytical thinking  

---

## 🚀 Business Value Delivered

The dashboard enables:

- Revenue monitoring at category and store level  
- Profitability optimization  
- Operational inefficiency identification  
- Seasonal demand planning  
- Short-term revenue forecasting  

This type of solution supports retail management in strategic and operational decision-making.

---

## 🔮 Future Enhancements

- Dynamic store ranking using DAX `RANKX`  
- Year-over-Year comparison  
- Store-level profitability breakdown  
- Advanced forecasting horizon  
- Migration to Power BI for enterprise deployment  

---

## 🏷 Keywords

Retail Analytics  
Business Intelligence  
Excel Dashboard  
DAX  
Power Pivot  
Data Modeling  
Time Series Forecasting  
Executive Reporting  

---

## 📌 Author

Adarsh Krishna  
Master’s in Data Science  
Focused on building business-oriented analytical solutions.
