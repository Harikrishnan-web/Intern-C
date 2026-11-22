# 1
# Python for Data Handling, Analysis and Visualization

## 1. CSV and JSON Handling

### CSV (Comma-Separated Values)
- Stores data in rows and columns.
- Values are separated by commas.
- Commonly used for storing tabular data.

**Reading CSV:**
```python
import pandas as pd

df = pd.read_csv("students.csv")
print(df)
```

**Writing CSV:**
```python
df.to_csv("output.csv", index=False)
```

### JSON (JavaScript Object Notation)
- Lightweight format for storing and exchanging data.
- Uses key-value pairs.
- Supports nested data structures.

**Reading JSON:**
```python
import pandas as pd

df = pd.read_json("student.json")
print(df)
```

**Writing JSON:**
```python
df.to_json("output.json", orient="records", indent=4)
```

| CSV | JSON |
|---|---|
| Stores tabular data | Stores structured data |
| Uses commas | Uses key-value pairs |
| Simple structure | Supports nested structures |

---

## 2. NumPy Arrays

### Definition
- NumPy stands for Numerical Python.
- Used for numerical and scientific calculations.
- Provides fast multidimensional arrays.

**Import NumPy:**
```python
import numpy as np
```

### Creating Arrays
```python
a = np.array([10, 20, 30, 40])
print(a)
```

### Important NumPy Functions

| Function | Purpose |
|---|---|
| `np.array()` | Creates an array |
| `np.zeros(5)` | Creates zeros |
| `np.ones(5)` | Creates ones |
| `np.arange(1, 10)` | Creates a sequence |
| `np.linspace(1, 10, 5)` | Creates evenly spaced values |
| `np.mean(a)` | Calculates mean |
| `np.max(a)` | Finds maximum |
| `np.min(a)` | Finds minimum |
| `np.sum(a)` | Calculates sum |
| `np.sort(a)` | Sorts array |

### Array Operations
```python
import numpy as np

a = np.array([10, 20, 30])

print(a + 5)
print(a * 2)
print(a - 5)
```

### Array Properties
```python
a = np.array([[1, 2], [3, 4]])

print(a.ndim)
print(a.shape)
print(a.size)
```

- `ndim`: Number of dimensions.
- `shape`: Number of rows and columns.
- `size`: Total number of elements.

---

## 3. Pandas Basics

### Definition
- Pandas is a Python library for data manipulation and analysis.
- Used to read, organize, clean and analyze datasets.
- Main data structures are Series and DataFrame.

**Import Pandas:**
```python
import pandas as pd
```

### Series
A one-dimensional labeled data structure.

```python
s = pd.Series([10, 20, 30, 40])
print(s)
```

### DataFrame
A two-dimensional structure containing rows and columns.

```python
data = {
    "Name": ["Arun", "Bala", "Ravi"],
    "Age": [20, 21, 19],
    "Marks": [85, 90, 75]
}

df = pd.DataFrame(data)
print(df)
```

### Important DataFrame Functions

| Function | Purpose |
|---|---|
| `head()` | Displays first 5 rows |
| `tail()` | Displays last 5 rows |
| `info()` | Displays column information |
| `describe()` | Statistical summary |
| `shape` | Number of rows and columns |
| `columns` | Displays column names |
| `dtypes` | Displays data types |
| `isnull()` | Checks missing values |
| `value_counts()` | Counts unique values |
| `sort_values()` | Sorts data |

### Selecting Rows and Columns
```python
print(df["Name"])
print(df[["Name", "Marks"]])

print(df.iloc[0])
print(df.loc[0])
```

- `iloc`: Selects rows using integer positions.
- `loc`: Selects rows using labels.

---

## 4. Statistical Measures

Consider the dataset:

```python
data = [10, 20, 20, 30, 40]
```

### 4.1 Mean
Mean is the average of all values.

**Formula:**

Mean = Sum of values / Number of values

```python
import numpy as np

data = [10, 20, 20, 30, 40]
print(np.mean(data))
```

Output: `24.0`

### 4.2 Median
Median is the middle value when data is arranged in ascending or descending order.

- Odd number of values: Middle value.
- Even number of values: Average of two middle values.

```python
print(np.median(data))
```

Output: `20.0`

### 4.3 Mode
Mode is the value that occurs most frequently.

```python
from statistics import mode

data = [10, 20, 20, 30, 40]
print(mode(data))
```

Output: `20`

Using Pandas:
```python
import pandas as pd

s = pd.Series([10, 20, 20, 30, 40])
print(s.mode())
```

### 4.4 Variance
Variance measures how far data values are spread from the mean.

- Low variance: Values are close to the mean.
- High variance: Values are widely spread.

**Population variance formula:**

Variance = Sum of squared deviations / Number of values

```python
import numpy as np

data = [10, 20, 20, 30, 40]

print(np.var(data))
```

Output: `104.0`

**Sample variance:**
```python
print(np.var(data, ddof=1))
```

### 4.5 Standard Deviation
Standard deviation measures the amount of variation or spread in a dataset.

**Formula:**

Standard Deviation = Square root of Variance

```python
import numpy as np

data = [10, 20, 20, 30, 40]

print(np.std(data))
```

**Sample standard deviation:**
```python
print(np.std(data, ddof=1))
```

| Measure | Meaning |
|---|---|
| Mean | Average |
| Median | Middle value |
| Mode | Most frequent value |
| Variance | Squared spread from mean |
| Standard deviation | Spread in original units |

---

## 5. IQR and Outlier Detection

### Outliers
Outliers are values that are significantly different from other values in a dataset.

Example:
```text
10, 12, 13, 15, 16, 18, 100
```

Here, `100` may be an outlier.

### Interquartile Range (IQR)
IQR measures the spread of the middle 50% of the data.

**Formula:**

IQR = Q3 - Q1

- Q1: First quartile (25th percentile).
- Q2: Second quartile (50th percentile or median).
- Q3: Third quartile (75th percentile).

### Outlier Detection Formula

Lower limit = Q1 - 1.5 × IQR

Upper limit = Q3 + 1.5 × IQR

Values outside these limits are considered potential outliers.

### Python Program
```python
import numpy as np

data = [10, 12, 13, 15, 16, 18, 100]

Q1 = np.percentile(data, 25)
Q3 = np.percentile(data, 75)

IQR = Q3 - Q1

lower = Q1 - 1.5 * IQR
upper = Q3 + 1.5 * IQR

outliers = [x for x in data if x < lower or x > upper]

print("Q1:", Q1)
print("Q3:", Q3)
print("IQR:", IQR)
print("Outliers:", outliers)
```

---

## 6. Missing Values

### Definition
Missing values occur when some data entries are empty or unavailable.

In Pandas, missing values are commonly represented by `NaN`.

### Detecting Missing Values
```python
print(df.isnull())
print(df.isnull().sum())
```

### Removing Missing Values
```python
df.dropna(inplace=True)
```

### Filling Missing Values with Zero
```python
df.fillna(0, inplace=True)
```

### Filling with Mean
```python
df["Age"] = df["Age"].fillna(df["Age"].mean())
```

### Filling with Median
```python
df["Marks"] = df["Marks"].fillna(df["Marks"].median())
```

| Function | Purpose |
|---|---|
| `isnull()` | Checks missing values |
| `dropna()` | Removes missing values |
| `fillna()` | Replaces missing values |

---

## 7. Duplicate Values

### Definition
Duplicate records are repeated rows or entries in a dataset.

### Detecting Duplicates
```python
print(df.duplicated())
```

### Counting Duplicates
```python
print(df.duplicated().sum())
```

### Removing Duplicates
```python
df.drop_duplicates(inplace=True)
```

| Function | Purpose |
|---|---|
| `duplicated()` | Identifies duplicate rows |
| `drop_duplicates()` | Removes duplicate rows |

---

## 8. Data Types in Pandas

Data types describe the kind of values stored in a column.

| Data Type | Description | Example |
|---|---|---|
| `int64` | Integer numbers | 10, 20 |
| `float64` | Decimal numbers | 10.5 |
| `object` | Usually text or mixed values | Arun |
| `bool` | True or False | True |
| `datetime64` | Date and time | 2026-11-22 |

### Checking Data Types
```python
print(df.dtypes)
```

### Changing Data Types

Convert into integer:
```python
df["Age"] = df["Age"].astype(int)
```

Convert into string:
```python
df["Name"] = df["Name"].astype(str)
```

Convert into datetime:
```python
df["Date"] = pd.to_datetime(df["Date"])
```

---

## 9. Matplotlib

### Definition
- Matplotlib is a Python library used for data visualization.
- It represents data using graphs and charts.
- Helps identify patterns, trends and comparisons.

**Import:**
```python
import matplotlib.pyplot as plt
```

### 9.1 Line Plot
Used to display trends over time or continuous data.

```python
x = [1, 2, 3, 4]
y = [10, 20, 15, 30]

plt.plot(x, y)
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("Line Plot")
plt.show()
```

### 9.2 Bar Chart
Used to compare different categories.

```python
names = ["Arun", "Bala", "Ravi"]
marks = [85, 90, 75]

plt.bar(names, marks)
plt.title("Student Marks")
plt.xlabel("Students")
plt.ylabel("Marks")
plt.show()
```

### 9.3 Histogram
Used to display the frequency distribution of numerical data.

```python
marks = [40, 50, 60, 60, 70, 80, 90]

plt.hist(marks, bins=5)
plt.title("Marks Distribution")
plt.show()
```

### 9.4 Scatter Plot
Used to show the relationship between two numerical variables.

```python
x = [1, 2, 3, 4, 5]
y = [10, 20, 15, 30, 25]

plt.scatter(x, y)
plt.title("Scatter Plot")
plt.show()
```

### Important Matplotlib Functions

| Function | Purpose |
|---|---|
| `plot()` | Line graph |
| `bar()` | Bar chart |
| `hist()` | Histogram |
| `scatter()` | Scatter plot |
| `xlabel()` | X-axis label |
| `ylabel()` | Y-axis label |
| `title()` | Graph title |
| `legend()` | Displays legend |
| `show()` | Displays graph |
| `savefig()` | Saves graph |

---

## 10. Seaborn

### Definition
- Seaborn is a Python data visualization library.
- It is built on top of Matplotlib.
- Provides attractive and informative statistical graphs.
- Works well with Pandas DataFrames.

**Import:**
```python
import seaborn as sns
import matplotlib.pyplot as plt
```

### 10.1 Count Plot
Used to count the number of observations in each category.

```python
data = ["Male", "Female", "Male", "Female", "Male"]

sns.countplot(x=data)
plt.show()
```

### 10.2 Box Plot
Used to visualize data distribution, median, quartiles and potential outliers.

```python
marks = [40, 50, 60, 70, 80, 90, 150]

sns.boxplot(x=marks)
plt.show()
```

### 10.3 Heatmap
Used to display values using different colors.

Commonly used to visualize correlation matrices.

```python
import pandas as pd

data = pd.DataFrame({
    "Math": [80, 90, 70],
    "Science": [85, 95, 75],
    "English": [70, 80, 60]
})

sns.heatmap(data.corr(), annot=True)
plt.show()
```

### 10.4 Pair Plot
Used to visualize relationships between multiple numerical variables.

```python
df = sns.load_dataset("iris")

sns.pairplot(df, hue="species")
```

### 10.5 Distribution Plot
Used to visualize the distribution of numerical data.

```python
marks = [40, 50, 60, 70, 80, 90]

sns.histplot(marks, kde=True)
plt.show()
```

### Important Seaborn Functions

| Function | Purpose |
|---|---|
| `countplot()` | Counts categories |
| `boxplot()` | Shows distribution and outliers |
| `heatmap()` | Displays values using colors |
| `pairplot()` | Shows relationships between variables |
| `histplot()` | Shows frequency distribution |
| `scatterplot()` | Shows relationships |
| `barplot()` | Compares numerical values across categories |

---

## 11. Matplotlib vs Seaborn

| Matplotlib | Seaborn |
|---|---|
| Basic visualization library | Statistical visualization library |
| More manual customization | Attractive default styles |
| Supports different graph types | Focuses on statistical graphs |
| Works with lists and arrays | Integrates well with Pandas |
| More control over graph elements | Easier statistical visualization |

---

## 12. Quick Revision – Important Python Syntax

| Task | Python Syntax |
|---|---|
| Import NumPy | `import numpy as np` |
| Import Pandas | `import pandas as pd` |
| Read CSV | `pd.read_csv("file.csv")` |
| Read JSON | `pd.read_json("file.json")` |
| Create array | `np.array([1,2,3])` |
| Create DataFrame | `pd.DataFrame(data)` |
| Display first rows | `df.head()` |
| Statistical summary | `df.describe()` |
| Calculate mean | `df.mean()` |
| Calculate median | `df.median()` |
| Calculate mode | `df.mode()` |
| Calculate variance | `df.var()` |
| Calculate standard deviation | `df.std()` |
| Check missing values | `df.isnull().sum()` |
| Remove missing values | `df.dropna()` |
| Fill missing values | `df.fillna(0)` |
| Check duplicates | `df.duplicated()` |
| Remove duplicates | `df.drop_duplicates()` |
| Check data types | `df.dtypes` |
| Change data type | `df.astype(int)` |
| Line graph | `plt.plot()` |
| Bar graph | `plt.bar()` |
| Histogram | `plt.hist()` |
| Scatter plot | `plt.scatter()` |
| Box plot | `sns.boxplot()` |
| Heatmap | `sns.heatmap()` |

---

## 13. Complete Python Data Analysis Example

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Create dataset
data = {
    "Name": ["Arun", "Bala", "Ravi", "Kumar", "Arun"],
    "Marks": [85, 90, 75, np.nan, 85],
    "Age": [20, 21, 19, 22, 20]
}

df = pd.DataFrame(data)

# Display dataset
print(df)

# Statistical analysis
print("Mean:", df["Marks"].mean())
print("Median:", df["Marks"].median())
print("Mode:", df["Marks"].mode())
print("Variance:", df["Marks"].var())
print("Standard Deviation:", df["Marks"].std())

# Missing values
print("Missing Values:")
print(df.isnull().sum())

# Fill missing values
df["Marks"] = df["Marks"].fillna(df["Marks"].mean())

# Remove duplicates
df = df.drop_duplicates()

# Check data types
print(df.dtypes)

# Histogram
sns.histplot(df["Marks"], kde=True)
plt.title("Marks Distribution")
plt.show()

# Box plot
sns.boxplot(x=df["Marks"])
plt.title("Marks Box Plot")
plt.show()
```

---

## 14. Important Points to Remember

1. NumPy is used for numerical calculations and arrays.
2. Pandas is used for data manipulation and analysis.
3. CSV stores data in rows and columns.
4. JSON stores data in key-value format.
5. Mean represents the average.
6. Median represents the middle value.
7. Mode represents the most frequent value.
8. Variance measures squared data spread.
9. Standard deviation measures data spread in original units.
10. IQR helps identify potential outliers.
11. `dropna()` removes missing values.
12. `fillna()` replaces missing values.
13. `drop_duplicates()` removes repeated records.
14. `dtypes` checks data types.
15. Matplotlib and Seaborn are used for data visualization.
---
