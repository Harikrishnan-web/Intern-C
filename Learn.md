# **1.Python for Data Handling, Data Analysis & Visualization**

These notes cover CSV and JSON handling, NumPy, Pandas, statistical calculations, data cleaning, and visualization using Matplotlib and Seaborn.

The focus is on **understanding the concepts and remembering the Python code needed to perform them.**

# **1. CSV and JSON Handling**

## **1.1 CSV (Comma-Separated Values)**

- CSV is a file format used to store tabular data.
- Data is arranged in rows and columns.
- Each value is separated by a comma.
- Commonly used for storing datasets.

**Example CSV file (**`students.csv`**):**

```
Name,Age,Marks
Arun,20,85
Bala,21,90
Ravi,19,75
```

**Reading a CSV file using Pandas:**

```
import pandas as pddf = pd.read_csv("students.csv")print(df)
```

**Writing data into a CSV file:**

```
df.to_csv("output.csv", index=False)
```

- `read_csv()` – Reads a CSV file.
- `to_csv()` – Saves data into a CSV file.
- `index=False` – Prevents saving the row index.

## **1.2 JSON (JavaScript Object Notation)**

- JSON is a lightweight data format used to store and exchange data.
- It stores information using key-value pairs.
- Supports objects, arrays, strings, numbers, Boolean values and null.

**Example JSON file (**`student.json`**):**

```
{
    "name": "Arun",
    "age": 20,
    "marks": 85
}
```

**Reading JSON:**

```
import pandas as pddf = pd.read_json("student.json")print(df)
```

**Writing JSON:**

```
df.to_json("output.json", orient="records", indent=4)
```

- `read_json()` – Reads JSON data.
- `to_json()` – Converts data into JSON format.
- `orient="records"` – Stores each row as a separate object.
- `indent=4` – Makes the output readable.

**Difference between CSV and JSON**

| CSV                       | JSON                                |
| ------------------------- | ----------------------------------- |
| Stores tabular data       | Stores structured data              |
| Uses commas               | Uses key-value pairs                |
| Simple structure          | Supports nested structures          |
| Suitable for spreadsheets | Suitable for APIs and data exchange |

# **2. NumPy Arrays**

## **What is NumPy?**

- NumPy stands for Numerical Python.
- It is a Python library used for numerical calculations.
- It provides fast and efficient multidimensional arrays.
- It is useful for mathematical and scientific operations.

**Import NumPy:**

```
import numpy as np
```

## **Creating arrays**

```
import numpy as npa = np.array([10, 20, 30, 40])print(a)
```

Output:

```
[10 20 30 40]
```

## **Important NumPy functions**

| Function                | Purpose                      |
| ----------------------- | ---------------------------- |
| `np.array()`            | Creates an array             |
| `np.zeros(5)`           | Creates an array of zeros    |
| `np.ones(5)`            | Creates an array of ones     |
| `np.arange(1, 10)`      | Creates a sequence           |
| `np.linspace(1, 10, 5)` | Creates evenly spaced values |
| `np.mean(a)`            | Calculates mean              |
| `np.max(a)`             | Finds maximum                |
| `np.min(a)`             | Finds minimum                |
| `np.sum(a)`             | Calculates sum               |
| `np.sort(a)`            | Sorts array                  |

## **Array operations**

```
import numpy as npa = np.array([10, 20, 30])print(a + 5)print(a * 2)print(a - 5)
```

Output:

```
[15 25 35]
[20 40 60]
[ 5 15 25]
```

## **Dimensions and shape**

```
a = np.array([[1, 2], [3, 4]])print(a.ndim)print(a.shape)print(a.size)
```

- `ndim` – Number of dimensions.
- `shape` – Number of rows and columns.
- `size` – Total number of elements.

# **3. Pandas Basics**

## **What is Pandas?**

- Pandas is a Python library used for data manipulation and analysis.
- It helps read, organize, clean and analyze datasets.
- It works mainly with two data structures: Series and DataFrame.

**Import Pandas:**

```
import pandas as pd
```

## **3.1 Series**

A Series is a one-dimensional labeled data structure.

```
import pandas as pds = pd.Series([10, 20, 30, 40])print(s)
```

## **3.2 DataFrame**

A DataFrame is a two-dimensional structure containing rows and columns.

```
import pandas as pddata = {    "Name": ["Arun", "Bala", "Ravi"],    "Age": [20, 21, 19],    "Marks": [85, 90, 75]}df = pd.DataFrame(data)print(df)
```

## **Important DataFrame functions**

| Function         | Purpose                      |
| ---------------- | ---------------------------- |
| `head()`         | Displays first 5 rows        |
| `tail()`         | Displays last 5 rows         |
| `info()`         | Displays column information  |
| `describe()`     | Displays statistical summary |
| `shape`          | Displays rows and columns    |
| `columns`        | Displays column names        |
| `dtypes`         | Displays data types          |
| `isnull()`       | Checks missing values        |
| `value_counts()` | Counts unique values         |
| `sort_values()`  | Sorts data                   |

Example:

```
print(df.head())print(df.describe())print(df.shape)print(df.columns)
```

## **Selecting columns and rows**

```
print(df["Name"])print(df[["Name", "Marks"]])print(df.iloc[0])print(df.loc[0])
```

- `iloc` – Selects rows using integer positions.
- `loc` – Selects rows using labels.

# **4. Statistical Measures**

Statistical measures help us understand and summarize numerical data.

Consider this dataset:

```
data = [10, 20, 20, 30, 40]
```

## **4.1 Mean**

Mean is the average of all values.

Formula:

\\[ Mean = \frac{\text{Sum of values}}{\text{Number of values}} \\]

Python:

```
import numpy as npdata = [10, 20, 20, 30, 40]print(np.mean(data))
```

Output: `24.0`

## **4.2 Median**

Median is the middle value when data is arranged in ascending or descending order.

- Odd number of values: Middle value.
- Even number of values: Average of two middle values.

Python:

```
import numpy as npdata = [10, 20, 20, 30, 40]print(np.median(data))
```

Output: `20.0`

## **4.3 Mode**

Mode is the value that occurs most frequently.

Python:

```
from statistics import modedata = [10, 20, 20, 30, 40]print(mode(data))
```

Output: `20`

Alternative using Pandas:

```
import pandas as pds = pd.Series([10, 20, 20, 30, 40])print(s.mode())
```

## **4.4 Variance**

Variance measures how far data values are spread from the mean.

- Low variance: Values are close to the mean.
- High variance: Values are widely spread.

Population variance:

\\[ \sigma^2 = \frac{\sum(x-\mu)^2}{N} \\]

Python:

```
import numpy as npdata = [10, 20, 20, 30, 40]print(np.var(data))
```

Output: `104.0`

For sample variance, use:

```
print(np.var(data, ddof=1))
```

## **4.5 Standard Deviation**

Standard deviation measures the amount of variation or spread in a dataset.

It is the square root of variance.

\\[ \sigma = \sqrt{\text{Variance}} \\]

Python:

```
import numpy as npdata = [10, 20, 20, 30, 40]print(np.std(data))
```

Output: `10.198`

For sample standard deviation:

```
print(np.std(data, ddof=1))
```

\\(\sigma = \sqrt{\frac{1}{N}\sum\_{i=1}^{N}(x_i-\mu)^2}\\)

The points have mean μ = 5 and σ = 1.5.

\\(\sigma\\)

Drag points

μ − σμ + σμ0246810

Give feedback

**Remember:**

| Measure            | Meaning                  |
| ------------------ | ------------------------ |
| Mean               | Average                  |
| Median             | Middle value             |
| Mode               | Most frequent value      |
| Variance           | Squared spread from mean |
| Standard deviation | Spread in original units |

# **5. IQR and Outlier Detection**

## **What is an Outlier?**

An outlier is a value that is significantly different from other values in a dataset.

Example:

```
10, 12, 13, 15, 16, 18, 100
```

Here, `100` may be an outlier.

## **What is IQR?**

IQR stands for Interquartile Range.

It measures the spread of the middle 50% of the data.

\\[ IQR = Q3 - Q1 \\]

- Q1 – First quartile (25th percentile).
- Q2 – Second quartile (50th percentile or median).
- Q3 – Third quartile (75th percentile).

## **Outlier detection formula**

Lower limit:

\\[ Q1 - 1.5 \times IQR \\]

Upper limit:

\\[ Q3 + 1.5 \times IQR \\]

Values outside these limits are considered potential outliers.

## **Python code**

```
import numpy as npdata = [10, 12, 13, 15, 16, 18, 100]Q1 = np.percentile(data, 25)Q3 = np.percentile(data, 75)IQR = Q3 - Q1lower = Q1 - 1.5 * IQRupper = Q3 + 1.5 * IQRoutliers = [x for x in data if x < lower or x > upper]print("Q1:", Q1)print("Q3:", Q3)print("IQR:", IQR)print("Outliers:", outliers)
```

**Important:** Outliers are not always errors. They should be investigated before removing them.

# **6. Missing Values**

## **What are Missing Values?**

Missing values occur when some data entries are empty or unavailable.

In Pandas, missing values are commonly represented by `NaN`.

Example:

| Name | Age | Marks |
| ---- | --- | ----- |
| Arun | 20  | 85    |
| Bala | NaN | 90    |
| Ravi | 19  | NaN   |

## **Detecting missing values**

```
print(df.isnull())
```

Count missing values in each column:

```
print(df.isnull().sum())
```

## **Removing missing values**

```
df.dropna(inplace=True)
```

Removes rows containing missing values.

## **Filling missing values**

Fill with zero:

```
df.fillna(0, inplace=True)
```

Fill with mean:

```
df["Age"] = df["Age"].fillna(df["Age"].mean())
```

Fill with median:

```
df["Marks"] = df["Marks"].fillna(df["Marks"].median())
```

**Remember:**

- `dropna()` – Removes missing values.
- `fillna()` – Replaces missing values.
- Mean is often useful for relatively symmetric numerical data without strong outliers.
- Median is often preferred when numerical data contains outliers.

# **7. Duplicate Values**

## **What are Duplicates?**

Duplicate records are repeated rows or entries in a dataset.

Example:

| Name | Age |
| ---- | --- |
| Arun | 20  |
| Bala | 21  |
| Arun | 20  |

Here, Arun's record is duplicated.

## **Detecting duplicates**

```
print(df.duplicated())
```

Count duplicates:

```
print(df.duplicated().sum())
```

## **Removing duplicates**

```
df.drop_duplicates(inplace=True)
```

**Important functions:**

- `duplicated()` – Identifies duplicate rows.
- `drop_duplicates()` – Removes duplicate rows.

# **8. Data Types in Pandas**

Data types describe the kind of values stored in a column.

| Data type    | Description                  | Example    |
| ------------ | ---------------------------- | ---------- |
| `int64`      | Integer numbers              | 10, 20     |
| `float64`    | Decimal numbers              | 10.5       |
| `object`     | Usually text or mixed values | Arun       |
| `bool`       | True or False                | True       |
| `datetime64` | Date and time                | 2026-11-22 |

## **Checking data types**

```
print(df.dtypes)
```

## **Changing data types**

Convert a column into integer:

```
df["Age"] = df["Age"].astype(int)
```

Convert into string:

```
df["Name"] = df["Name"].astype(str)
```

Convert into datetime:

```
df["Date"] = pd.to_datetime(df["Date"])
```

**Why is it important?**

- Ensures correct calculations.
- Prevents data processing errors.
- Helps organize and analyze datasets properly.

# **9. Matplotlib**

## **What is Matplotlib?**

- Matplotlib is a Python library used for data visualization.
- It helps represent data using graphs and charts.
- It is useful for identifying patterns, trends and comparisons.

Import:

```
import matplotlib.pyplot as plt
```

## **9.1 Line Plot**

Used to display trends over time or continuous data.

```
import matplotlib.pyplot as pltx = [1, 2, 3, 4]y = [10, 20, 15, 30]plt.plot(x, y)plt.xlabel("X-axis")plt.ylabel("Y-axis")plt.title("Line Plot")plt.show()
```

## **9.2 Bar Chart**

Used to compare different categories.

```
import matplotlib.pyplot as pltnames = ["Arun", "Bala", "Ravi"]marks = [85, 90, 75]plt.bar(names, marks)plt.title("Student Marks")plt.xlabel("Students")plt.ylabel("Marks")plt.show()
```

## **9.3 Histogram**

Used to display the frequency distribution of numerical data.

```
import matplotlib.pyplot as pltmarks = [40, 50, 60, 60, 70, 80, 90]plt.hist(marks, bins=5)plt.title("Marks Distribution")plt.show()
```

## **9.4 Scatter Plot**

Used to show the relationship between two numerical variables.

```
import matplotlib.pyplot as pltx = [1, 2, 3, 4, 5]y = [10, 20, 15, 30, 25]plt.scatter(x, y)plt.title("Scatter Plot")plt.show()
```

## **Important Matplotlib functions**

| Function    | Purpose         |
| ----------- | --------------- |
| `plot()`    | Line graph      |
| `bar()`     | Bar chart       |
| `hist()`    | Histogram       |
| `scatter()` | Scatter plot    |
| `xlabel()`  | X-axis label    |
| `ylabel()`  | Y-axis label    |
| `title()`   | Graph title     |
| `legend()`  | Displays legend |
| `show()`    | Displays graph  |
| `savefig()` | Saves graph     |

# **10. Seaborn**

## **What is Seaborn?**

- Seaborn is a Python data visualization library.
- It is built on top of Matplotlib.
- It provides attractive and informative statistical graphs.
- It works well with Pandas DataFrames.

Import:

```
import seaborn as snsimport matplotlib.pyplot as plt
```

## **10.1 Count Plot**

Used to count the number of observations in each category.

```
import seaborn as snsimport matplotlib.pyplot as pltdata = ["Male", "Female", "Male", "Female", "Male"]sns.countplot(x=data)plt.show()
```

## **10.2 Box Plot**

Used to visualize data distribution, median, quartiles and potential outliers.

```
import seaborn as snsimport matplotlib.pyplot as pltmarks = [40, 50, 60, 70, 80, 90, 150]sns.boxplot(x=marks)plt.show()
```

## **10.3 Heatmap**

Used to display values using different colors.

Commonly used to visualize correlation matrices.

```
import seaborn as snsimport matplotlib.pyplot as pltimport pandas as pddata = pd.DataFrame({    "Math": [80, 90, 70],    "Science": [85, 95, 75],    "English": [70, 80, 60]})sns.heatmap(data.corr(), annot=True)plt.show()
```

## **10.4 Pair Plot**

Used to visualize relationships between multiple numerical variables.

```
import seaborn as snsdf = sns.load_dataset("iris")sns.pairplot(df, hue="species")
```

## **10.5 Distribution Plot**

Used to visualize the distribution of numerical data.

```
import seaborn as snsimport matplotlib.pyplot as pltmarks = [40, 50, 60, 70, 80, 90]sns.histplot(marks, kde=True)plt.show()
```

## **Important Seaborn functions**

| Function        | Purpose                                     |
| --------------- | ------------------------------------------- |
| `countplot()`   | Counts categories                           |
| `boxplot()`     | Shows distribution and outliers             |
| `heatmap()`     | Displays values using colors                |
| `pairplot()`    | Shows relationships between variables       |
| `histplot()`    | Shows frequency distribution                |
| `scatterplot()` | Shows relationships                         |
| `barplot()`     | Compares numerical values across categories |

# **11. Matplotlib vs Seaborn**

| Matplotlib                       | Seaborn                           |
| -------------------------------- | --------------------------------- |
| Basic visualization library      | Statistical visualization library |
| More manual customization        | Attractive default styles         |
| Supports different graph types   | Focuses on statistical graphs     |
| Works with lists and arrays      | Integrates well with Pandas       |
| More control over graph elements | Easier statistical visualization  |

# **12. Quick Revision – Important Python Syntax**

This is the most important section to revise before performing practical tasks.

| Task                         | Python syntax               |
| ---------------------------- | --------------------------- |
| Import NumPy                 | `import numpy as np`        |
| Import Pandas                | `import pandas as pd`       |
| Read CSV                     | `pd.read_csv("file.csv")`   |
| Read JSON                    | `pd.read_json("file.json")` |
| Create array                 | `np.array([1,2,3])`         |
| Create DataFrame             | `pd.DataFrame(data)`        |
| Display first rows           | `df.head()`                 |
| Statistical summary          | `df.describe()`             |
| Calculate mean               | `df.mean()`                 |
| Calculate median             | `df.median()`               |
| Calculate mode               | `df.mode()`                 |
| Calculate variance           | `df.var()`                  |
| Calculate standard deviation | `df.std()`                  |
| Check missing values         | `df.isnull().sum()`         |
| Remove missing values        | `df.dropna()`               |
| Fill missing values          | `df.fillna(0)`              |
| Check duplicates             | `df.duplicated()`           |
| Remove duplicates            | `df.drop_duplicates()`      |
| Check data types             | `df.dtypes`                 |
| Change data type             | `df.astype(int)`            |
| Line graph                   | `plt.plot()`                |
| Bar graph                    | `plt.bar()`                 |
| Histogram                    | `plt.hist()`                |
| Scatter plot                 | `plt.scatter()`             |
| Box plot                     | `sns.boxplot()`             |
| Heatmap                      | `sns.heatmap()`             |

# **13. Complete Python Data Analysis Example**

This program combines several topics into one practical example. You can use it as a reference for practical examinations.

```
import pandas as pdimport numpy as npimport matplotlib.pyplot as pltimport seaborn as sns# Create datasetdata = {    "Name": ["Arun", "Bala", "Ravi", "Kumar", "Arun"],    "Marks": [85, 90, 75, np.nan, 85],    "Age": [20, 21, 19, 22, 20]}df = pd.DataFrame(data)# Display datasetprint(df)# Statistical analysisprint("Mean:", df["Marks"].mean())print("Median:", df["Marks"].median())print("Mode:", df["Marks"].mode())print("Variance:", df["Marks"].var())print("Standard Deviation:", df["Marks"].std())# Missing valuesprint("Missing Values:")print(df.isnull().sum())df["Marks"] = df["Marks"].fillna(df["Marks"].mean())# Remove duplicatesdf = df.drop_duplicates()# Check data typesprint(df.dtypes)
```

# **14. Important Points to Remember**

1. NumPy is mainly used for numerical calculations and arrays.
2. Pandas is used for data manipulation and analysis.
3. CSV stores data in rows and columns.
4. JSON stores data in key-value format.
5. Mean represents the average.
6. Median represents the middle value.
7. Mode represents the most frequent value.
8. Variance measures squared data spread.
9. Standard deviation measures data spread in the original units.
10. IQR helps identify potential outliers.
11. `dropna()` removes missing values.
12. `fillna()` replaces missing values.
13. `drop_duplicates()` removes repeated records.
14. `dtypes` checks data types.
15. Matplotlib and Seaborn are used for visualization.

---
