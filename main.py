# Step 1: Import libraries
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Step 2: Load the dataset
df = pd.read_csv("sales_data.csv")

# Step 3: Explore the data
print("First 5 rows:")
print(df.head())
print("\nSummary info:")
print(df.info())
print("\nBasic statistics:")
print(df.describe())

# Step 4: Total sales by region
region_sales = df.groupby("Region")["Sales"].sum().sort_values(ascending=False)
print("\nTotal Sales by Region:\n", region_sales)

plt.figure(figsize=(8,5))
ax = sns.barplot(x=region_sales.index, y=region_sales.values, palette="coolwarm")
plt.title("Total Sales by Region")
plt.xlabel("Region")
plt.ylabel("Total Sales")

# Add value labels on top of bars
for container in ax.containers:
    ax.bar_label(container, fmt='%.0f', label_type='edge', padding=3)

plt.show()


# Step 5: Top-selling products
top_products = df.groupby("Product")["Sales"].sum().sort_values(ascending=False)
print("\nTop-Selling Products:\n", top_products)

plt.figure(figsize=(8,5))
ax = sns.barplot(x=top_products.index, y=top_products.values, palette="viridis")
plt.title("Top-Selling Products")
plt.xlabel("Product")
plt.ylabel("Total Sales")

# Add value labels
for container in ax.containers:
    ax.bar_label(container, fmt='%.0f', label_type='edge', padding=3)

plt.show()
