# Retail Sales Performance Analysis — AAL

## Overview

This project analyzes three months (October–December) of sales data for AAL, a U.S.-based apparel retailer serving kids, women, men, and seniors across multiple states and city tiers. With the business in active expansion mode, the goal is to turn raw transaction-level data into clear, actionable insights that support investment and growth decisions.

## Business Context

AAL has grown from a single clothing brand into a nationwide retailer with stores in metros, tier-1, and tier-2 cities. As leadership considers where and how to invest next, they need a data-driven view of:

- How unit sales and revenue have trended over the quarter
- How performance varies month to month
- Which states and regions are driving (or lagging in) sales
- Patterns across product groups and time that could inform inventory, staffing, or expansion decisions

## Objectives

- Clean and prepare the raw sales dataset for analysis
- Normalize key metrics to allow fair comparison across scales
- Visualize overall and monthly sales/unit trends
- Summarize statistical distributions for units sold and revenue
- Break down performance by state, group, and time period
- Surface insights that support expansion and investment decisions

## Dataset

- **Source file:** `Sales.csv`
- **Granularity:** Daily transaction-level data
- **Time period:** October – December (one sales season)
- **Key fields:** Date, State, Unit (units sold), Sales (revenue)

## Approach

1. **Data Preparation** — Load and inspect the dataset; check dimensions and confirm there are no missing values.
2. **Normalization** — Scale the Unit and Sales columns to a common 0–1 range so they can be compared and analyzed consistently.
3. **Overall Trend Analysis** — Plot daily Unit and Sales totals across the full season to spot broad patterns.
4. **Monthly Breakdown** — Split the data into October, November, and December subsets for month-over-month comparison.
5. **Descriptive Statistics** — Generate summary statistics (mean, std, min, max, quartiles) for the full period and for each month.
6. **Distribution Analysis** — Use boxplots to examine the spread and outliers in units sold and sales revenue by month.
7. **Consolidated Visuals** — Combine overall and monthly plots into a single view of the season's performance.
8. **Statewise Analysis** — Compare sales performance across states to identify top and underperforming markets.
9. **Groupwise Analysis** — Compare performance across customer/product groups.
10. **Time-based Analysis** — Explore patterns by day, week, or other time cuts to identify seasonality or trends.

## Tools & Libraries

- Python
- pandas — data manipulation and analysis
- NumPy — numerical operations
- scikit-learn — data normalization (`MinMaxScaler` / `Normalizer`)
- Matplotlib / Seaborn — data visualization

## Project Structure

```
├── Sales.csv                 # Raw dataset
├── sales_analysis.ipynb      # Main analysis notebook
└── README.md                 # Project documentation
```

## How to Run

1. Clone or download this repository
2. Install dependencies:
   ```
   pip install pandas numpy scikit-learn matplotlib seaborn
   ```
3. Open `sales_analysis.ipynb` in Jupyter Notebook or JupyterLab
4. Run the cells in order to reproduce the analysis and visualizations

## Key Questions This Analysis Answers

- What does overall sales and unit volume look like across the quarter?
- How does performance shift from October to November to December?
- Which states contribute the most (and least) to total sales?
- Are there notable patterns by customer group or time period that could inform strategy?

---

*This is a self-directed data analysis project exploring retail sales trends using Python's data science stack.*
