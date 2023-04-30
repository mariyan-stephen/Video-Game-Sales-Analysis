import pandas as pd

# Read the CSV file
data = pd.read_csv("vgsales.csv")

# Clean the data
data.drop_duplicates(inplace=True)
data['Year'].fillna(data['Year'].median(), inplace=True)
data.dropna(subset=['Publisher'], inplace=True)

# Perform basic data analysis
print("Number of rows and columns:", data.shape)

print("\nAverage sales by region:")
print("NA_Sales:", data['NA_Sales'].mean())
print("EU_Sales:", data['EU_Sales'].mean())
print("JP_Sales:", data['JP_Sales'].mean())
print("Other_Sales:", data['Other_Sales'].mean())

print("\nTop 5 platforms:")
print(data['Platform'].value_counts().head(5))

print("\nTop 5 genres:")
print(data['Genre'].value_counts().head(5))

print("\nTop 5 publishers:")
print(data['Publisher'].value_counts().head(5))

# Export the results
summary_statistics = data.describe()
summary_statistics.index.name = "Statistic"
summary_statistics.to_csv("summary_statistics.csv")

