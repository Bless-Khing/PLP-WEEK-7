import matplotlib.pyplot as plt
import seaborn as sns

# Set the style for seaborn
sns.set(style="whitegrid")

# Line chart showing trends over time (assuming we have a time series)
# For demonstration, we will create a dummy time series
time_data = pd.DataFrame({
    'time': range(1, 11),
    'sepal_length': [5.1, 4.9, 4.7, 4.6, 5.0, 5.4, 5.5, 5.6, 5.7, 5.8]
})
plt.figure(figsize=(10, 6))
plt.plot(time_data['time'], time_data['sepal_length'], marker='o')
plt.title('Sepal Length Over Time')
plt.xlabel('Time')
plt.ylabel('Sepal Length')
plt.grid(True)
plt.show()

# Bar chart showing average sepal length per species
plt.figure(figsize=(10, 6))
sns.barplot(x=grouped_data.index, y=grouped_data.values)
plt.title('Average Sepal Length per Species')
plt.xlabel('Species')
plt.ylabel('Average Sepal Length')
plt.show()

# Histogram of sepal length distribution
plt.figure(figsize=(10, 6))
sns.histplot(df['sepal_length'], bins=10, kde=True)
plt.title('Distribution of Sepal Length')
plt.xlabel('Sepal Length')
plt.ylabel('Frequency')
plt.show()

# Scatter plot to visualize relationship between sepal length and petal length
plt.figure(figsize=(10, 6))
sns.scatterplot(x='sepal_length', y='petal_length', hue='species', data=df)
plt.title('Sepal Length vs Petal Length')
plt.xlabel('Sepal Length')
plt.ylabel('Petal Length')
plt.legend(title='Species')
plt.show()
