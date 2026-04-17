import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("sales_data.csv")

# Show data
print(df.head())

# Structure
print(df.info())
print(df.describe())

# Create total sales column
df['total_sales'] = df['quantity'] * df['price']

# Total revenue
print("Total Revenue:", df['total_sales'].sum())

# Most sold product
print(df.groupby('product')['quantity'].sum())

# Sales by city
print(df.groupby('city')['total_sales'].sum())

# Bar chart
df.groupby('product')['total_sales'].sum().plot(kind='bar')
plt.title("Product vs Sales")
plt.show()

# Pie chart
df.groupby('category')['total_sales'].sum().plot(kind='pie', autopct='%1.1f%%')
plt.title("Category Distribution")
plt.show()

# Line chart
df.groupby('order_date')['total_sales'].sum().plot(kind='line')
plt.title("Sales Over Time")
plt.show()