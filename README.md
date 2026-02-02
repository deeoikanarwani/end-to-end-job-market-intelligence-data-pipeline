## Job Market Analysis & Salary Prediction

## Overview --
This project builds an end-to-end data pipeline to analyze job market trends and predict salaries for data-related roles.

## Workflow --
- Extracted job listings data
- Cleaned and transformed salary, company, and location features
- Performed exploratory data analysis (EDA)
- Engineered features and trained a regression model
- Evaluated model using MAE and R² score

## Tech Stack --
- Python
- Pandas, NumPy
- Scikit-learn
- Matplotlib

## Outcome --
- Identified key salary drivers such as company rating and size
- Built a salary prediction model for job listings

 
## Output --
 ## Dataset Summary

| Metric | Value |
|------|------|
| Total Records | 2252 |
| Total Features | 20 |
| Numeric Columns | 4 |
| Categorical/Text Columns | 16 |
| Memory Usage | ~370 KB |

## Dataset Columns

| Column Name | Description |
|------------|------------|
| Job Title | Job role title |
| Salary Estimate | Salary range from job listing |
| Job Description | Full job description text |
| Rating | Company rating |
| Company Name | Name of the company |
| Location | Job location |
| Headquarters | Company headquarters |
| Size | Company size |
| Founded | Year company was founded |
| Type of ownership | Ownership type |
| Industry | Industry domain |
| Sector | Business sector |
| Revenue | Company revenue |
| Competitors | Competitor companies |
| Easy Apply | Easy apply availability |
| avg_salary | Calculated average salary |
| City | Extracted city |
| State | Extracted state |
| Company Age | Company age in years |
| Has Competitors | Binary competitor flag |

## Numerical Feature Statistics

| Feature | Mean | Min | Max |
|-------|------|-----|-----|
| Founded | 1398 | -1 | 2019 |
| Average Salary | 72.12 | 33.5 | 150 |
| Company Age | 45.65 | 5 | 342 |
| Has Competitors | 0.23 | 0 | 1 |

## Numerical Feature Statistics

| Feature | Mean | Min | Max |
|-------|------|-----|-----|
| Founded | 1398 | -1 | 2019 |
| Average Salary | 72.12 | 33.5 | 150 |
| Company Age | 45.65 | 5 | 342 |
| Has Competitors | 0.23 | 0 | 1 |

## Top Paying Roles

| Job Title | Avg Salary |
|----------|------------|
| Tableau Data Analyst Intern | 150 |
| AI Insights Data Analyst | 150 |
| Sr. Data Analyst – Growth & Adoption | 150 |
| Senior HR Data Analyst | 150 |
| Data Analyst (SQL, Hive) | 150 |

## Most In-Demand Skills

| Skill | Frequency |
|------|-----------|
| SQL | 1388 |
| Excel | 1353 |
| Python | 637 |
| Tableau | 620 |
| Power BI | 180 |
| Machine Learning | 180 |
| Pandas | 41 |
| NumPy | 23 |
| NLP | 16 |
| Deep Learning | 11 |

## Model Evaluation

| Model | MAE | R² Score |
|------|-----|----------|
| Linear Regression | 17.05 | -0.01 |
| Random Forest | 18.74 | -0.15 |

## Top Important Features (Random Forest)

| Feature | Importance |
|--------|------------|
| Company Age | 0.4087 |
| Rating | 0.2806 |
| Excel | 0.0575 |
| Tableau | 0.0504 |
| Has Competitors | 0.0487 |
| SQL | 0.0468 |
| Python | 0.0334 |
| Machine Learning | 0.0270 |
| Power BI | 0.0256 |
| Pandas | 0.0066 |

## Saved Models

| Artifact | Status |
|--------|--------|
| Cleaned Dataset | ✅ Saved |
| Linear Regression Model | ✅ Saved |
| Random Forest Model | ✅ Saved |


