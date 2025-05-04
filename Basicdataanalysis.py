# Compute basic statistics
print(df.describe())

# Group by species and compute the mean
grouped_mean = df.groupby('species').mean()
print(grouped_mean)

# Identify patterns
print("Observation: Sepal and petal sizes differ noticeably between species.")
