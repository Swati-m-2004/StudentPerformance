import pandas as pd

# Load the dataset
df = pd.read_csv("student_performance.csv")

print("========== DATASET EXPLORATION ==========")

# 1. Display first five records
print("\n--- First Five Records ---")
print(df.head())

# 2. Display last five records
print("\n--- Last Five Records ---")
print(df.tail())

# 3. Dataset dimensions
print("\n--- Dataset Shape ---")
print("Rows:", df.shape[0])
print("Columns:", df.shape[1])
print("Shape:", df.shape)

# 4. Column names
print("\n--- Column Names ---")
print(df.columns.tolist())

# 5. Dataset information
print("\n--- Dataset Info ---")
df.info()

# 6. Statistical summary
print("\n--- Descriptive Statistics ---")
print(df.describe())

# 7. Data types
print("\n--- Data Types ---")
print(df.dtypes)

# 8. Numerical and categorical columns
numerical_columns = df.select_dtypes(include="number").columns.tolist()
categorical_columns = df.select_dtypes(include="object").columns.tolist()

print("\n--- Numerical Columns ---")
print(numerical_columns)

print("\n--- Categorical Columns ---")
print(categorical_columns)

# 9. Missing values
print("\n--- Missing Values ---")
print(df.isnull().sum())

# 10. At least five observations
print("\n--- Observations ---")
print("1. The dataset contains", df.shape[0], "student records.")
print("2. The dataset contains", df.shape[1], "columns.")
print("3. Study_Hours, Attendance, Math_Score and Final_Score are numerical.")
print("4. Name is a categorical/text column.")
print("5. Final_Score has a mean of", round(df["Final_Score"].mean(), 2))
print("6. The highest Final_Score is", df["Final_Score"].max())
print("7. The lowest Final_Score is", df["Final_Score"].min())
print("8. Missing values in the dataset:", int(df.isnull().sum().sum()))
