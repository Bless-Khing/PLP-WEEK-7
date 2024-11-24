# Compute basic statistics of numerical columns
print("\nBasic Statistics:")
print(df.describe())

# Perform groupings on a categorical column (species) and compute mean of a numerical column (sepal length)
grouped_data = df.groupby('species')['sepal_length'].mean()
print("\nMean Sepal Length per Species:")
print(grouped_data)

# Identify interesting findings
max_sepal_length = df['sepal_length'].max()
min_sepal_length = df['sepal_length'].min()
print(f"\nMaximum Sepal Length: {max_sepal_length}")
print(f"Minimum Sepal Length: {min_sepal_length}")
