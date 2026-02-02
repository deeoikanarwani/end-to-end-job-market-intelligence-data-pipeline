# ================================
# 1. IMPORT LIBRARIES
# ================================
import pandas as pd
import re
import joblib

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, r2_score


# ================================
# 2. LOAD DATA
# ================================
df = pd.read_csv("data/raw/DataAnalyst.csv")

print(df.head())
print(df.columns)

# Drop unnecessary index column
df.drop(columns=["Unnamed: 0"], inplace=True)


# ================================
# 3. CLEAN SALARY DATA
# ================================
def clean_salary(salary):
    if pd.isna(salary) or salary == "-1":
        return None

    salary = salary.replace("(Glassdoor est.)", "")
    salary = salary.replace("$", "").replace("K", "")

    numbers = re.findall(r"\d+", salary)

    if len(numbers) == 2:
        return (int(numbers[0]) + int(numbers[1])) / 2
    elif len(numbers) == 1:
        return int(numbers[0])
    else:
        return None

df["avg_salary"] = df["Salary Estimate"].apply(clean_salary)

# Remove rows without salary
df = df[df["avg_salary"].notna()]


# ================================
# 4. CLEAN COMPANY NAME
# ================================
df["Company Name"] = (
    df["Company Name"]
    .astype(str)
    .str.split("\n")
    .str[0]
)


# ================================
# 5. BASIC FEATURE ENGINEERING
# ================================
df["Rating"] = df["Rating"].replace(-1, None)

df["City"] = df["Location"].str.split(",").str[0]
df["State"] = df["Location"].str.split(",").str[1]

df["Company Age"] = df["Founded"].apply(
    lambda x: 2024 - x if x > 0 else None
)

df["Has Competitors"] = df["Competitors"].apply(
    lambda x: 0 if x == "-1" else 1
)


# ================================
# 6. SAVE CLEAN DATA
# ================================
df.to_csv("data/cleaned_jobs.csv", index=False)
print("✅ Cleaned data saved successfully!")


# ================================
# 7. QUICK EDA
# ================================
print(df.info())
print(df.describe())

print(
    df.groupby("Job Title")["avg_salary"]
      .mean()
      .sort_values(ascending=False)
      .head(10)
)

print(df[["Rating", "avg_salary"]].corr())


# ================================
# 8. BASELINE ML MODEL (LINEAR REGRESSION)
# ================================
base_features = [
    "Rating",
    "Company Age",
    "Has Competitors"
]

df_base = df[base_features + ["avg_salary"]].dropna()

X = df_base[base_features]
y = df_base["avg_salary"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

lr = LinearRegression()
lr.fit(X_train, y_train)

lr_pred = lr.predict(X_test)

print("Linear Regression MAE:", mean_absolute_error(y_test, lr_pred))
print("Linear Regression R2:", r2_score(y_test, lr_pred))

joblib.dump(lr, "models/salary_model.pkl")
print("✅ Linear Regression model saved")


# ================================
# 9. NLP – SKILL EXTRACTION
# ================================
skills = [
    "python", "sql", "excel", "tableau", "power bi",
    "machine learning", "deep learning", "nlp",
    "pandas", "numpy", "scikit-learn"
]

def skill_extractor(description):
    description = description.lower()
    return [skill for skill in skills if skill in description]

df["Skills"] = df["Job Description"].fillna("").apply(skill_extractor)

for skill in skills:
    df[skill] = df["Skills"].apply(lambda x: 1 if skill in x else 0)

print("Skill demand:")
print(df[skills].sum().sort_values(ascending=False))


# ================================
# 10. ADVANCED ML – RANDOM FOREST
# ================================
rf_features = base_features + skills

df_rf = df[rf_features + ["avg_salary"]].dropna()

X = df_rf[rf_features]
y = df_rf["avg_salary"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

rf = RandomForestRegressor(
    n_estimators=200,
    random_state=42
)

rf.fit(X_train, y_train)

rf_pred = rf.predict(X_test)

print("Random Forest MAE:", mean_absolute_error(y_test, rf_pred))
print("Random Forest R2:", r2_score(y_test, rf_pred))


# ================================
# 11. FEATURE IMPORTANCE (NO ERROR NOW)
# ================================
importance = pd.Series(
    rf.feature_importances_,
    index=X.columns
).sort_values(ascending=False)

print("Top important features:")
print(importance.head(10))

print("Feature count check:")
print(len(rf.feature_importances_), len(X.columns))


# ================================
# 12. SAVE FINAL MODEL
# ================================
joblib.dump(rf, "models/salary_model_rf.pkl")
print("✅ Random Forest model saved")
