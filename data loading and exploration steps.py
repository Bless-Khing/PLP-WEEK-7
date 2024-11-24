import pandas as pd

# Load the Iris dataset
try:
    df = pd.read_csv('iris.csv')  # Replace with your CSV file path
    print("Dataset loaded successfully.")
except FileNotFoundError:
    print("Error: The file was not found.")
    exit()
except Exception as e:
    print(f"An error occurred: {e}")
    exit()

# Display the first few rows of the dataset
print(df.head())

# Explore the structure of the dataset
print("\nData Types:")
print(df.dtypes)

print("\nMissing Values:")
print(df.isnull().sum())

# Clean the dataset by filling or dropping missing values
df.fillna(method='ffill', inplace=True)  # Forward fill to handle missing values
print("\nMissing Values After Cleaning:")
print(df.isnull().sum())
