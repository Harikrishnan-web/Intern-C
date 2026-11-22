
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

csv_data = pd.read_csv("employees.csv")
json_data = pd.read_json("employees.json")

df = pd.concat([csv_data, json_data], ignore_index=True)

print("\nEMPLOYEE DETAILS")
print(df.to_string(index=False))

salary = df["Salary"]

print("\nSALARY STATISTICS")
print("Mean Salary:", round(np.mean(salary), 2))
print("Median Salary:", round(np.median(salary), 2))
print("Mode Salary:", salary.mode().tolist())
print("Standard Deviation:", round(np.std(salary), 2))

print("\nDEPARTMENT-WISE AVERAGE SALARY")
print(df.groupby("Department")["Salary"].mean().round(2))

q1 = np.percentile(salary, 25)
q3 = np.percentile(salary, 75)
iqr = q3 - q1

lower_limit = q1 - 1.5 * iqr
upper_limit = q3 + 1.5 * iqr

outliers = df[
    (df["Salary"] < lower_limit) |
    (df["Salary"] > upper_limit)
]

print("\nSALARY OUTLIERS")
print(outliers.to_string(index=False))

print("\nLOWER LIMIT:", lower_limit)
print("UPPER LIMIT:", upper_limit)

plt.figure(figsize=(8, 5))
sns.histplot(data=df, x="Salary", bins=8, kde=True)
plt.title("Employee Salary Distribution")
plt.xlabel("Salary")
plt.ylabel("Number of Employees")
plt.tight_layout()
plt.show()

plt.figure(figsize=(8, 5))
sns.barplot(data=df, x="Department", y="Salary", errorbar=None)
plt.title("Department-wise Average Salary")
plt.xlabel("Department")
plt.ylabel("Average Salary")
plt.tight_layout()
plt.show()

plt.figure(figsize=(8, 5))
sns.boxplot(data=df, x="Salary")
plt.title("Salary Outlier Detection")
plt.xlabel("Salary")
plt.tight_layout()
plt.show()

df.to_csv("employee_salary_analysis_output.csv", index=False)

print("\nAnalysis completed successfully!")
