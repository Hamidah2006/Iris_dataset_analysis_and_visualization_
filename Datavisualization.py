# Set seaborn style
sns.set(style='whitegrid')

# Line chart (for illustration, cumulative mean of petal length per species)
df_sorted = df.sort_values(by='petal length (cm)')
for species in df['species'].unique():
    subset = df_sorted[df_sorted['species'] == species]
    plt.plot(subset['petal length (cm)'].cumsum(), label=species)
plt.title("Cumulative Petal Length by Species")
plt.xlabel("Sample Index")
plt.ylabel("Cumulative Petal Length")
plt.legend()
plt.show()

# Bar chart: Average sepal width by species
sns.barplot(x='species', y='sepal width (cm)', data=df)
plt.title("Average Sepal Width by Species")
plt.show()

# Histogram: Distribution of petal length
plt.hist(df['petal length (cm)'], bins=20, color='skyblue', edgecolor='black')
plt.title("Distribution of Petal Length")
plt.xlabel("Petal Length (cm)")
plt.ylabel("Frequency")
plt.show()

# Scatter plot: Sepal length vs. petal length
sns.scatterplot(x='sepal length (cm)', y='petal length (cm)', hue='species', data=df)
plt.title("Sepal Length vs. Petal Length")
plt.show()
