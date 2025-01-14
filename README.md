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

The data cleaning and preprocessing are performed in the `2025-VeloCityX-Data Cleaning.ipynb` script. The main steps include:

1. **Initial Exploration**: Load the dataset and perform initial exploration to understand its structure and contents.
2. **Remove Duplicates**: Remove duplicate rows from the dataset.
3. **Handle Missing Values**: Fill missing values with the mean of the respective columns.
4. **Fix Structural Errors**: Correct any structural errors or typos in the dataset (example provided but commented out).
5. **Normalize or Standardize Data**: Normalize or standardize numerical columns if necessary (example provided but commented out).

## Analysis and Modeling

The analysis and modeling steps are performed in the `2025-VeloCityX-Data Analysis.ipynb` script. The main steps include:

1. **Investigate Trends**: Identify which users will most likely purchase virtual merchandise and analyze user activities during race events.
2. **Clustering**: Apply KMeans clustering to identify user segments based on their activities.
3. **Predictive Modeling**: Use a Random Forest Classifier to predict virtual merchandise purchases based on user activities.
4. **Evaluation**: Evaluate the predictive model using classification reports and confusion matrices.

## Results

The results of the analysis and modeling are visualized using various plots, including scatter plots and heatmaps. Key insights about user behavior are identified and discussed.
