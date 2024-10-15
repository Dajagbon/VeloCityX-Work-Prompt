import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the data
df = pd.read_csv('C:/Users/danie/Downloads/2025-VeloCityX-Expanded-Fan-Engagement-Data-cleaned.csv')

# Initial exploration
print("Initial DataFrame:")
print(df.head())
print(df.info())
print(df.describe())

# Group by user and calculate the total virtual merchandise purchased
user_merch_purchases = df.groupby('User ID')['Virtual Merchandise Purchases'].sum().reset_index()

# Sort users by the total virtual merchandise purchased
top_users = user_merch_purchases.sort_values(by='Virtual Merchandise Purchases', ascending=False)

print("\nTop users most likely to purchase virtual merchandise:")
print(top_users.head())

# Analyze Fan Challenges Completed during race events and their correlation with merchandise purchases and sponsorship interactions
# Correlation matrix
correlation_matrix = df[['Fan Challenges Completed', 'Virtual Merchandise Purchases', 'Sponsorship Interactions (Ad Clicks)']].corr()

print("\nCorrelation matrix:")
print(correlation_matrix)

# Visualize the correlation matrix
plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f')
plt.title('Correlation Matrix of Fan Challenges Completed, Merchandise Purchases, and Sponsorship Interaction')
plt.show()

# Scatter plot to visualize the relationship between race event activity and virtual merchandise purchases
plt.figure(figsize=(10, 6))
sns.scatterplot(data=df, x='Fan Challenges Completed', y='Virtual Merchandise Purchases', hue='Sponsorship Interactions (Ad Clicks)', palette='viridis')
plt.title('Fan Challenges Completed vs. Virtual Merchandise Purchases')
plt.xlabel('Fan Challenges Completed')
plt.ylabel('Virtual Merchandise Purchases')
plt.show()