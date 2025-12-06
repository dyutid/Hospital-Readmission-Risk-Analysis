# Hospital-Readmission-Risk-Analysis
This project is to analyze key factors contributing to higher readmission ratios and develop a data driven dashboard summarizing hospital performance by condition and region.

# Dataset Information
Primary Dataset

Name: FY 2025 Hospital Readmissions Reduction Program (HRRP)

Source: Centers for Medicare & Medicaid Services (CMS)

Link: https://data.cms.gov/provider-data/dataset/9n3s-kdb3

Format: CSV

Size: ~3,200 hospital-condition records

License: Public U.S. Government dataset

# Dataset Description

This dataset measures hospital performance in reducing 30-day readmission rates for Medicare patients across six major clinical conditions. Each hospital appears multiple times—once for each condition—allowing analysis at both the hospital-level and condition-level.

It includes hospital identifiers, geographic information, condition types, readmission ratios, predicted vs. expected rates, patient volumes, and payment penalty adjustments.

# Key Columns
Column	Description	Type
Provider ID	Unique hospital identifier	String
Hospital Name	Name of hospital	String
State, ZIP	Geographic location	String
Measure Name	Medical condition	String
Excess Readmission Ratio	Observed vs expected benchmark	Float
Number of Cases	Patients included	Integer
Predicted Rate	Predicted readmission percentage	Float
Expected Rate	National benchmark rate	Float
Payment Reduction	Penalty percentage applied	Float
# Objectives

The primary goal is to analyze factors contributing to higher readmission ratios and develop a data-driven, interactive dashboard summarizing hospital performance by condition and region.

# Research Questions

Which hospitals and states have the highest and lowest readmission ratios?

How do readmission rates vary across clinical conditions (e.g., Heart Failure, COPD, Pneumonia)?

Is there a relationship between hospital size (number of cases) and readmission performance?

Which hospitals receive the largest payment penalties?

Which conditions contribute the most to national readmission penalties?

# Tools & Methodology
Technology Stack

Python

pandas, numpy

matplotlib, seaborn, plotly

scikit-learn

statsmodels

Streamlit / Plotly Dash

# Workflow
A. Data Preparation

      Load dataset using pandas
      
      Handle missing values and type conversions
      
      Normalize hospital and condition names
      
      Aggregate data by hospital and by state

B. Exploratory Data Analysis (EDA)

      Summary statistics
      
      Distribution plots and boxplots
      
      Identify extreme performers
      
      Correlation heatmaps for:
      
      Readmission ratios
      
      Number of cases
      
      Payment penalties

C. Hypothesis Testing

      Hypothesis:
      
      H₀: No relationship exists between hospital size and readmission ratios
      
      H₁: Hospital size significantly affects readmission ratios
      
      Tests Used:
      
      Independent t-tests
      
      One-way ANOVA

D. Modeling & Insights

      Multiple Linear Regression to evaluate predictors of readmission ratio
      
      K-Means Clustering to segment hospitals by performance and penalty risk
      
      Feature analysis includes:
      
      Expected rates
      
      Case volume
      
      Condition type
      
      Payment penalties

E. Dashboard Development

      Built using Streamlit with:
      
      Top and bottom performing hospitals
      Readmissions by condition
      State-level penalty heatmap
      Relationship between penalties & readmissions
      Hospital comparison filters

# How to Run
pip install pandas numpy matplotlib seaborn plotly scikit-learn statsmodels streamlit
streamlit run dashboard.py
