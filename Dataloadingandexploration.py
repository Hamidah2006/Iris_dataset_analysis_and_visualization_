# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris

# Load the Iris dataset
try:
    iris = load_iris()
    df = pd.DataFrame(data=iris.data, columns=iris.feature_names)
    df['species'] = iris.target
    df['species'] = df['species'].map({i: name for i, name in enumerate(iris.target_names)})
except Exception as e:
    print("Error loading dataset:", e)

# Display the first few rows
print(df.head())

# Check data types and missing values
print(df.info())
print(df.isnull().sum())

# Clean dataset (in this case, no missing values, so nothing to clean)
