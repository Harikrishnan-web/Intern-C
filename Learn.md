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
# 2
# Python for Machine Learning – Supervised and Unsupervised Learning

## 1. Supervised vs Unsupervised Learning

### Supervised Learning

- Supervised learning is a machine learning technique where a model learns from labelled data.
- Labelled data contains input features and known output values.
- The model learns the relationship between inputs and outputs to make predictions.

**Types:**
1. Regression – Predicts continuous numerical values.
2. Classification – Predicts categories or classes.

**Examples:**
- Predicting house prices.
- Email spam detection.
- Predicting student marks.

**Python Example:**
```python
from sklearn.linear_model import LinearRegression

model = LinearRegression()
model.fit(X_train, y_train)

predictions = model.predict(X_test)
```

### Unsupervised Learning

- Unsupervised learning uses unlabelled data.
- There is no predefined output or target variable.
- The model identifies hidden patterns, groups and relationships in data.

**Types:**
1. Clustering – Groups similar data points.
2. Association – Identifies relationships between variables.
3. Dimensionality reduction – Reduces the number of features.

**Examples:**
- Customer segmentation.
- Grouping similar products.
- Finding patterns in customer behaviour.

**Python Example:**
```python
from sklearn.cluster import KMeans

model = KMeans(n_clusters=3, random_state=42)
model.fit(X)

print(model.labels_)
```

### Difference Between Supervised and Unsupervised Learning

| Supervised Learning | Unsupervised Learning |
|---|---|
| Uses labelled data | Uses unlabelled data |
| Has target output | No target output |
| Predicts outcomes | Finds hidden patterns |
| Classification and regression | Clustering and dimensionality reduction |
| Example: Spam detection | Example: Customer grouping |

---

## 2. Train-Test Split

### Definition

Train-test split is a technique used to divide a dataset into two parts.

1. Training data – Used to train the machine learning model.
2. Testing data – Used to evaluate model performance on unseen data.

**Common Splitting Ratios:**

| Training Data | Testing Data |
|---|---|
| 80% | 20% |
| 70% | 30% |
| 75% | 25% |

### Python Program

```python
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

print(X_train.shape)
print(X_test.shape)
```

**Important Parameters:**

- `X` – Input features.
- `y` – Target variable.
- `test_size=0.2` – Uses 20% for testing.
- `random_state=42` – Ensures reproducible splitting.

**Advantages:**
- Evaluates model performance.
- Helps identify overfitting.
- Tests predictions on unseen data.

---

## 3. Preprocessing Pipeline

### Definition

A preprocessing pipeline is a sequence of data preparation steps performed before training a machine learning model.

It helps ensure that data is processed consistently during training and prediction.

### Common Preprocessing Steps

1. Handling missing values.
2. Removing duplicate records when appropriate.
3. Encoding categorical data.
4. Scaling numerical features.
5. Splitting training and testing data.

### Important Preprocessing Techniques

**1. Missing Value Handling**

```python
from sklearn.impute import SimpleImputer

imputer = SimpleImputer(strategy="mean")
X = imputer.fit_transform(X)
```

**2. Feature Scaling**

```python
from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
```

**3. Encoding Categorical Data**

```python
from sklearn.preprocessing import OneHotEncoder

encoder = OneHotEncoder(handle_unknown="ignore")
```

### Creating a Pipeline

```python
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression

pipeline = Pipeline([
    ("imputer", SimpleImputer(strategy="mean")),
    ("scaler", StandardScaler()),
    ("model", LogisticRegression())
])

pipeline.fit(X_train, y_train)

predictions = pipeline.predict(X_test)
```

**Advantages:**
- Automates preprocessing.
- Reduces repeated code.
- Ensures consistent transformations.
- Helps prevent data leakage.

---

## 4. Data Leakage

### Definition

Data leakage occurs when information from outside the training data is used during model training.

It can make a machine learning model appear more accurate than it actually is.

### Types of Data Leakage

**1. Target Leakage**

- Occurs when information directly related to the target variable is included as an input feature.
- The model indirectly gets access to the answer.

**2. Train-Test Contamination**

- Occurs when test data influences the training process.
- Example: Scaling the entire dataset before splitting it.

### Example of Incorrect Approach

```python
from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()

X_scaled = scaler.fit_transform(X)

X_train, X_test, y_train, y_test = train_test_split(
    X_scaled, y, test_size=0.2, random_state=42
)
```

### Correct Approach

```python
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

scaler = StandardScaler()

X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)
```

**Important:**
- Use `fit_transform()` on training data.
- Use only `transform()` on testing data.
- Never use test data to learn preprocessing parameters.

---

## 5. Linear Regression

### Definition

Linear regression is a supervised machine learning algorithm used to predict continuous numerical values.

It identifies the linear relationship between independent and dependent variables.

**Examples:**
- Predicting house prices.
- Predicting salary.
- Predicting sales.
- Predicting student marks.

### Mathematical Formula

y = mx + c

Where:

- y = Predicted output.
- x = Input variable.
- m = Slope or coefficient.
- c = Intercept.

For multiple features:

y = b0 + b1x1 + b2x2 + ... + bnxn

### Python Program

```python
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score

X = [[1], [2], [3], [4], [5]]
y = [10, 20, 30, 40, 50]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = LinearRegression()

model.fit(X_train, y_train)

predictions = model.predict(X_test)

print("Predictions:", predictions)
print("R2 Score:", r2_score(y_test, predictions))
```

### Important Functions

| Function | Purpose |
|---|---|
| `LinearRegression()` | Creates model |
| `fit()` | Trains model |
| `predict()` | Makes predictions |
| `coef_` | Displays coefficients |
| `intercept_` | Displays intercept |

### Advantages
- Simple and easy to understand.
- Fast to train.
- Useful for predicting numerical values.

### Limitations
- Assumes a linear relationship.
- Sensitive to outliers.
- May perform poorly on complex relationships.

---

## 6. Logistic Regression

### Definition

Logistic regression is a supervised machine learning algorithm mainly used for classification problems.

It predicts the probability of an observation belonging to a particular class.

**Examples:**
- Spam or not spam.
- Pass or fail.
- Disease or no disease.
- Fraud or genuine transaction.

### Sigmoid Function

The sigmoid function converts a value into a probability between 0 and 1.

\[
P = \frac{1}{1+e^{-z}}
\]

Where:
- P = Predicted probability.
- e = Euler's number.
- z = Linear combination of input features.

### Python Program

```python
from sklearn.linear_model import LogisticRegression

X = [[1], [2], [3], [4], [5], [6]]
y = [0, 0, 0, 1, 1, 1]

model = LogisticRegression()

model.fit(X, y)

predictions = model.predict(X)

print("Predictions:", predictions)
print("Probabilities:", model.predict_proba(X))
```

### Important Functions

| Function | Purpose |
|---|---|
| `LogisticRegression()` | Creates model |
| `fit()` | Trains model |
| `predict()` | Predicts class |
| `predict_proba()` | Predicts class probabilities |

### Linear Regression vs Logistic Regression

| Linear Regression | Logistic Regression |
|---|---|
| Used for regression | Used for classification |
| Predicts continuous values | Predicts class probabilities |
| Uses linear equation | Uses sigmoid function |
| Example: House price | Example: Spam detection |

---

## 7. Confusion Matrix

### Definition

A confusion matrix is a table used to evaluate the performance of a classification model.

It compares actual values with predicted values.

### Four Important Terms

1. True Positive (TP): Model correctly predicts positive.
2. True Negative (TN): Model correctly predicts negative.
3. False Positive (FP): Model predicts positive but actual value is negative.
4. False Negative (FN): Model predicts negative but actual value is positive.

### Confusion Matrix Structure

| | Predicted Positive | Predicted Negative |
|---|---|---|
| Actual Positive | TP | FN |
| Actual Negative | FP | TN |

### Python Program

```python
from sklearn.metrics import confusion_matrix

actual = [1, 0, 1, 1, 0, 0]
predicted = [1, 0, 1, 0, 0, 1]

cm = confusion_matrix(actual, predicted)

print(cm)
```

Output:

```text
[[2 1]
 [1 2]]
```

### Visualizing Confusion Matrix

```python
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix

cm = confusion_matrix(actual, predicted)

sns.heatmap(cm, annot=True, fmt="d", cmap="Blues")

plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.title("Confusion Matrix")

plt.show()
```

---

## 8. Accuracy

### Definition

Accuracy measures the percentage of correctly predicted observations.

### Formula

\[
Accuracy = \frac{TP+TN}{TP+TN+FP+FN}
\]

### Python Program

```python
from sklearn.metrics import accuracy_score

actual = [1, 0, 1, 1, 0]
predicted = [1, 0, 1, 0, 0]

accuracy = accuracy_score(actual, predicted)

print("Accuracy:", accuracy)
```

Output:

```text
Accuracy: 0.8
```

Accuracy = 80%.

**Advantages:**
- Easy to understand.
- Useful when classes are reasonably balanced and error costs are similar.

**Limitation:**
- Can be misleading when the dataset is highly imbalanced.

---

## 9. Precision

### Definition

Precision measures how many of the observations predicted as positive are actually positive.

### Formula

\[
Precision = \frac{TP}{TP+FP}
\]

### Python Program

```python
from sklearn.metrics import precision_score

actual = [1, 0, 1, 1, 0]
predicted = [1, 0, 1, 0, 0]

precision = precision_score(actual, predicted)

print("Precision:", precision)
```

Output:

```text
Precision: 1.0
```

**Importance:**
- Useful when false positive predictions are costly.
- Example: Avoiding genuine emails being marked as spam.

### Other Important Evaluation Metrics

**Recall:**

Measures how many actual positive cases are correctly identified.

\[
Recall = \frac{TP}{TP+FN}
\]

**F1 Score:**

Harmonic mean of precision and recall.

\[
F1 = 2 \times \frac{Precision \times Recall}{Precision+Recall}
\]

Python:

```python
from sklearn.metrics import recall_score, f1_score

print("Recall:", recall_score(actual, predicted))
print("F1 Score:", f1_score(actual, predicted))
```

---

## 10. Classification Thresholds

### Definition

A classification threshold is the probability value used to decide whether a prediction belongs to the positive or negative class.

The default threshold in many binary classifiers is 0.5.

### Example

| Predicted Probability | Threshold | Predicted Class |
|---|---|---|
| 0.80 | 0.50 | Positive |
| 0.60 | 0.50 | Positive |
| 0.40 | 0.50 | Negative |
| 0.20 | 0.50 | Negative |

### Python Program

```python
probabilities = [0.8, 0.6, 0.4, 0.2]

threshold = 0.5

predictions = [
    1 if p >= threshold else 0
    for p in probabilities
]

print(predictions)
```

Output:

```text
[1, 1, 0, 0]
```

### Effect of Threshold

- Lower threshold: More positive predictions, generally higher recall and potentially lower precision.
- Higher threshold: Fewer positive predictions, generally higher precision and potentially lower recall.

Threshold selection depends on the cost of false positives and false negatives.

---

## 11. Decision Trees

### Definition

A decision tree is a supervised machine learning algorithm used for classification and regression.

It makes predictions using a tree-like structure of conditions and decisions.

### Main Components

1. Root Node – Starting point of the tree.
2. Decision Node – Represents a condition or test.
3. Branch – Represents the outcome of a decision.
4. Leaf Node – Represents the final prediction.

### Example

A decision tree can predict whether a student passes or fails based on marks.

```text
          Marks > 50?
           /      \
         Yes       No
          |         |
        Pass       Fail
```

### Python Program

```python
from sklearn.tree import DecisionTreeClassifier

X = [[30], [40], [50], [60], [70], [80]]
y = [0, 0, 0, 1, 1, 1]

model = DecisionTreeClassifier(random_state=42)

model.fit(X, y)

predictions = model.predict([[45], [75]])

print(predictions)
```

### Visualizing Decision Tree

```python
from sklearn.tree import plot_tree
import matplotlib.pyplot as plt

plot_tree(model, filled=True)

plt.show()
```

### Advantages
- Easy to understand.
- Handles numerical and categorical features.
- Requires little feature scaling.
- Can model nonlinear relationships.

### Limitations
- Can overfit.
- Small data changes can produce different trees.
- Deep trees may become complex.

---

## 12. Random Forests

### Definition

Random Forest is an ensemble machine learning algorithm that combines multiple decision trees to improve prediction performance.

It uses:
- Random samples of training data.
- Random subsets of features.
- Multiple decision trees.

### Working Principle

1. Creates multiple random samples from training data.
2. Builds a decision tree for each sample.
3. Each tree makes a prediction.
4. Combines predictions to produce the final result.

For classification, majority voting is generally used.

For regression, predictions are generally averaged.

### Python Program

```python
from sklearn.ensemble import RandomForestClassifier

X = [[30], [40], [50], [60], [70], [80]]
y = [0, 0, 0, 1, 1, 1]

model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

model.fit(X, y)

predictions = model.predict([[45], [75]])

print(predictions)
```

### Important Parameters

| Parameter | Purpose |
|---|---|
| `n_estimators` | Number of decision trees |
| `max_depth` | Maximum depth of each tree |
| `random_state` | Controls randomness |
| `max_features` | Number of features considered for splitting |
| `min_samples_split` | Minimum samples required to split a node |

### Advantages
- Often provides good prediction accuracy.
- Reduces overfitting compared with a single deep decision tree.
- Handles complex datasets.
- Can estimate feature importance.

### Limitations
- Requires more memory.
- Can be slower than a single decision tree.
- Less interpretable than an individual decision tree.

---

## 13. Tree Depth

### Definition

Tree depth refers to the maximum number of levels from the root node to a leaf node.

### Importance

- Shallow tree: Simpler model, may underfit.
- Deep tree: More complex model, may overfit.

### Python Program

```python
from sklearn.tree import DecisionTreeClassifier

model = DecisionTreeClassifier(
    max_depth=3,
    random_state=42
)

model.fit(X, y)
```

Here, `max_depth=3` limits the maximum tree depth to 3.

### Effect of Tree Depth

| Shallow Tree | Deep Tree |
|---|---|
| Simple model | Complex model |
| May underfit | May overfit |
| Less computation | More computation |
| Easier to interpret | Harder to interpret |

---

## 14. Feature Importance

### Definition

Feature importance measures how much each input feature contributes to a machine learning model's predictions.

It helps identify which variables are more influential in a model.

### Example

In house price prediction, important features may include:
- House area.
- Number of bedrooms.
- Location.
- Building age.

### Python Program

```python
from sklearn.ensemble import RandomForestClassifier
import pandas as pd

X = pd.DataFrame({
    "Age": [20, 30, 40, 50, 60],
    "Salary": [20000, 30000, 40000, 50000, 60000],
    "Experience": [1, 3, 5, 7, 9]
})

y = [0, 0, 0, 1, 1]

model = RandomForestClassifier(random_state=42)

model.fit(X, y)

importance = model.feature_importances_

for name, value in zip(X.columns, importance):
    print(name, value)
```

### Important Points

- Higher importance indicates greater contribution to the model's predictions.
- Lower importance indicates less contribution.
- Feature importance does not prove that a feature causes the outcome.
- Tree-based models such as Decision Trees and Random Forests provide feature importance values.

---

## 15. Important Python Libraries

| Library | Purpose |
|---|---|
| NumPy | Numerical calculations |
| Pandas | Data handling and analysis |
| Matplotlib | Data visualization |
| Seaborn | Statistical visualization |
| Scikit-learn | Machine learning |
| `sklearn.model_selection` | Train-test splitting |
| `sklearn.preprocessing` | Data preprocessing |
| `sklearn.pipeline` | Creating pipelines |
| `sklearn.linear_model` | Linear and logistic regression |
| `sklearn.tree` | Decision trees |
| `sklearn.ensemble` | Random forests |
| `sklearn.metrics` | Model evaluation |

---

## 16. Quick Revision – Important Python Syntax

| Task | Python Syntax |
|---|---|
| Import Scikit-learn | `import sklearn` |
| Split dataset | `train_test_split()` |
| Create linear regression | `LinearRegression()` |
| Create logistic regression | `LogisticRegression()` |
| Create decision tree | `DecisionTreeClassifier()` |
| Create random forest | `RandomForestClassifier()` |
| Train model | `model.fit(X_train, y_train)` |
| Make predictions | `model.predict(X_test)` |
| Predict probabilities | `model.predict_proba(X_test)` |
| Calculate accuracy | `accuracy_score()` |
| Calculate precision | `precision_score()` |
| Calculate recall | `recall_score()` |
| Calculate F1 score | `f1_score()` |
| Create confusion matrix | `confusion_matrix()` |
| Scale features | `StandardScaler()` |
| Fill missing values | `SimpleImputer()` |
| Create pipeline | `Pipeline()` |
| Display feature importance | `model.feature_importances_` |
| Set tree depth | `max_depth=3` |
| Plot decision tree | `plot_tree()` |

---

## 17. Important Points to Remember

1. Supervised learning uses labelled data.
2. Unsupervised learning uses unlabelled data.
3. Train-test split separates training and testing datasets.
4. Preprocessing prepares data before model training.
5. Data leakage occurs when information from outside the training process improperly influences the model.
6. Linear regression predicts continuous numerical values.
7. Logistic regression is used for classification.
8. Confusion matrix evaluates classification predictions.
9. Accuracy measures overall correct predictions.
10. Precision measures the correctness of positive predictions.
11. Recall measures how many actual positive cases are identified.
12. F1 score balances precision and recall.
13. Classification thresholds determine positive and negative predictions.
14. Decision trees use conditions to make predictions.
15. Random forests combine multiple decision trees.
16. Tree depth controls model complexity.
17. Feature importance identifies influential input features.

---
