# 2025 VeloCityX Expanded Fan Engagement Data Analysis

## Project Overview

This project aims to clean, organize, and analyze the 2025 VeloCityX Expanded Fan Engagement dataset. The dataset contains information about fan activities, virtual merchandise purchases, and sponsorship interactions. The primary objectives of this project are to:

1. Clean and preprocess the dataset.
2. Investigate trends and identify key insights about user behavior.
3. Apply clustering and predictive modeling techniques to gain deeper insights.
4. Visualize the trends and correlations in the data.

## Dataset

The dataset used in this project is located at:
`C:/Users/danie/Downloads/2025-VeloCityX-Expanded-Fan-Engagement-Data-cleaned`

### Columns in the Dataset

- `user_id`: Unique identifier for each user.
- `Fan Challenges Completed`: Number of fan challenges the user completes.
- `Virtual Merchandise Purchases`: Number of virtual merchandise items the user purchases.
- `Sponsorship Interactions (Ad Clicks)`: Number of sponsorship interactions (ad clicks) by the user.
- Additional columns are present in the dataset.

## Data Cleaning and Preprocessing

The data cleaning and preprocessing are performed in the `2025-VeloCityX-DataCleaning.py` script. The main steps include:

1. **Initial Exploration**: Load the dataset and perform initial exploration to understand its structure and contents.
2. **Remove Duplicates**: Remove duplicate rows from the dataset.
3. **Handle Missing Values**: Fill missing values with the mean of the respective columns.
4. **Fix Structural Errors**: Correct any structural errors or typos in the dataset (example provided but commented out).
5. **Normalize or Standardize Data**: Normalize or standardize numerical columns if necessary (example provided but commented out).

### Excerpt from `2025-VeloCityX-DataCleaning.py`

```python
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
