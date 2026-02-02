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
 Unnamed: 0  ... Easy Apply
0           0  ...       True
1           1  ...         -1
2           2  ...         -1
3           3  ...         -1
4           4  ...       True

[5 rows x 16 columns]
Index(['Unnamed: 0', 'Job Title', 'Salary Estimate', 'Job Description',    
       'Rating', 'Company Name', 'Location', 'Headquarters', 'Size', 'Founded',
       'Type of ownership', 'Industry', 'Sector', 'Revenue', 'Competitors',
       'Easy Apply'],
      dtype='str')
✅ Cleaned data saved successfully!
<class 'pandas.DataFrame'>
Index: 2252 entries, 0 to 2252
Data columns (total 20 columns):
 #   Column             Non-Null Count  Dtype
---  ------             --------------  -----
 0   Job Title          2252 non-null   str
 1   Salary Estimate    2252 non-null   str
 2   Job Description    2252 non-null   str
 3   Rating             1980 non-null   object
 4   Company Name       2251 non-null   object
 5   Location           2252 non-null   str
 6   Headquarters       2252 non-null   str
 7   Size               2252 non-null   str
 8   Founded            2252 non-null   int64
 9   Type of ownership  2252 non-null   str
 10  Industry           2252 non-null   str
 11  Sector             2252 non-null   str
 12  Revenue            2252 non-null   str
 13  Competitors        2252 non-null   str
 14  Easy Apply         2252 non-null   str
 15  avg_salary         2252 non-null   float64
 16  City               2252 non-null   object
 17  State              2252 non-null   object
 18  Company Age        1592 non-null   float64
 19  Has Competitors    2252 non-null   int64
dtypes: float64(2), int64(2), object(4), str(12)
memory usage: 369.5+ KB
None
           Founded   avg_salary  Company Age  Has Competitors
count  2252.000000  2252.000000  1592.000000      2252.000000
mean   1398.255329    72.123002    45.651382         0.231350
std     902.040151    23.600734    47.833946         0.421789
min      -1.000000    33.500000     5.000000         0.000000
25%      -1.000000    58.000000    18.000000         0.000000
50%    1979.000000    69.000000    27.000000         0.000000
75%    2002.000000    80.500000    54.000000         0.000000
max    2019.000000   150.000000   342.000000         1.000000
Job Title
Tableau Data Analyst Intern                       150.0
AI Insights Data Analyst                          150.0
Data Analyst with Data Mapping and API            150.0
Sr. Data Analyst - Growth & Adoption              150.0
Senior HR Data Analyst                            150.0
Data Analyst (SQL, Hive)                          150.0
Data Analyst, Autonomy Operations                 150.0
Senior Data Analyst Studio Finance Engineering    150.0
Data Analyst, Product Insights                    150.0
Data Studio Analyst                               138.5
Name: avg_salary, dtype: float64
             Rating  avg_salary
Rating      1.00000     0.04256
avg_salary  0.04256     1.00000
Linear Regression MAE: 17.05613508910633
Linear Regression R2: -0.011600385019441273
✅ Linear Regression model saved
Skill demand:
sql                 1388
excel               1353
python               637
tableau              620
power bi             180
machine learning     180
pandas                41
numpy                 23
nlp                   16
deep learning         11
scikit-learn           8
dtype: int64
Random Forest MAE: 18.74462828455989
Random Forest R2: -0.1549307474120032
Top important features:
Company Age         0.408676
Rating              0.280590
excel               0.057545
tableau             0.050389
Has Competitors     0.048745
sql                 0.046807
python              0.033364
machine learning    0.027024
power bi            0.025609
pandas              0.006563
dtype: float64
Feature count check:
14 14
✅ Random Forest model saved
