import pandas as pd

# Load the data
df = pd.read_csv('C:/Users/danie/Downloads/2025-VeloCityX-Expanded-Fan-Engagement-Data.csv')

# Initial exploration
print("Initial DataFrame:")
print(df.head())
print(df.info())
print(df.describe())

# Store the initial state of the DataFrame
initial_shape = df.shape
initial_missing_values = df.isnull().sum()

# Remove duplicates
df.drop_duplicates(inplace=True)

# Handle missing values
df.fillna(df.mean(numeric_only=True), inplace=True)

# Fix structural errors (example: correcting typos in a specific column)
# df['column_name'].replace({'typo1': 'correct1', 'typo2': 'correct2'}, inplace=True)

# Normalize or standardize data if necessary
# Example: Standardizing numerical columns
# from sklearn.preprocessing import StandardScaler
# scaler = StandardScaler()
# df[['numerical_column1', 'numerical_column2']] = scaler.fit_transform(df[['numerical_column1', 'numerical_column2']])

# Store the final state of the DataFrame
final_shape = df.shape
final_missing_values = df.isnull().sum()

# Compare the initial and final states
print("\nChanges in the DataFrame:")
print(f"Initial shape: {initial_shape}")
print(f"Final shape: {final_shape}")
print(f"Number of duplicates removed: {initial_shape[0] - final_shape[0]}")

print("\nInitial missing values:")
print(initial_missing_values)
print("\nFinal missing values:")
print(final_missing_values)
print("\nNumber of missing values filled:")
print(initial_missing_values - final_missing_values)

# Save the cleaned dataset to a new CSV file
df.to_csv('C:/Users/danie/Downloads/2025-VeloCityX-Expanded-Fan-Engagement-Data-cleaned.csv', index=False)