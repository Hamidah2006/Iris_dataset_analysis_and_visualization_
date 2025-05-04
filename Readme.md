# Iris Dataset Analysis Assignment

## Objective

This assignment demonstrates the use of Python for data analysis and visualization. It involves loading the Iris dataset, performing basic data analysis, and generating visual insights using libraries such as `pandas`, `matplotlib`, and `seaborn`.

---

## Dataset

**Iris Dataset**: A well-known dataset in machine learning and statistics, containing 150 records of iris flowers classified into three species with four features:
- Sepal length (cm)
- Sepal width (cm)
- Petal length (cm)
- Petal width (cm)

---

## Tools and Libraries

- **Python 3**
- **pandas** – for data manipulation
- **matplotlib** – for basic plotting
- **seaborn** – for improved visualization styling
- **scikit-learn** – to load the Iris dataset

---

## Tasks Completed

### Task 1: Data Loading and Exploration
- Loaded the dataset using `sklearn.datasets.load_iris()`.
- Converted the data into a pandas DataFrame.
- Displayed the first few rows with `.head()`.
- Checked for missing values and data types using `.info()` and `.isnull().sum()`.

### Task 2: Basic Data Analysis
- Calculated basic statistics with `.describe()`.
- Grouped the data by species and computed the mean values of numerical columns.
- Identified species differences based on petal and sepal measurements.

### Task 3: Data Visualization
1. **Line Chart** – Cumulative petal length by species.
2. **Bar Chart** – Average sepal width across species.
3. **Histogram** – Distribution of petal length values.
4. **Scatter Plot** – Sepal length vs. petal length colored by species.

All visualizations are clearly labeled with titles, axes, and legends for better interpretation.

## Observations

- The dataset is clean and does not contain missing values.
- Petal length is a strong distinguishing feature between species.
- Versicolor and virginica show more overlap than setosa, which is distinctly different.

---

## Author

**Olaniyi Hamidah Olaitan**
