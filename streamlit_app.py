# This script uses the pandas library to load, analyze, and summarize data
# from the 'sales_data.csv' file in the same directory.

import pandas as pd
import os

# Define the file path for the data
FILE_PATH = 'sales_data.csv'

# --- 1. Load the Data ---
try:
    # Read the CSV file into a pandas DataFrame (a 2D labeled data structure)
    df = pd.read_csv(FILE_PATH)
    print("✅ Data successfully loaded from sales_data.csv\n")
except FileNotFoundError:
    print(f"Error: The file '{FILE_PATH}' was not found. Make sure it is in the same folder.")
    exit()
except Exception as e:
    print(f"An unexpected error occurred during file loading: {e}")
    exit()

# --- 2. Data Overview ---
print("--- Data Overview ---")
# Print the first few rows of the data
print(df.head())
print(f"\nTotal rows loaded: {len(df)}")
print("-" * 25 + "\n")


# --- 3. Perform Aggregation (Calculate Total Revenue) ---
# Sum the values in the 'Revenue' column for a grand total.
total_revenue = df['Revenue'].sum()
print("--- Total Summary ---")
print(f"💰 Grand Total Revenue: ${total_revenue:,.2f}")
print("-" * 25 + "\n")


# --- 4. Filtering (Find High-Performance Sales) ---
# Filter the DataFrame to show only rows where UnitsSold is greater than 100.
high_sales_filter = df['UnitsSold'] > 100
high_sales_df = df[high_sales_filter]

print("--- High-Performance Sales (Units > 100) ---")
if not high_sales_df.empty:
    print("These sales lines sold over 100 units:")
    print(high_sales_df[['Month', 'Product', 'UnitsSold']])
else:
    print("No sales lines exceeded 100 units sold.")
print("-" * 25 + "\n")


# --- 5. Grouping and Aggregation (Revenue by Product) ---
# Group the data by the 'Product' column and sum the 'Revenue' for each product.
revenue_by_product = df.groupby('Product')['Revenue'].sum().reset_index()

print("--- Revenue Breakdown by Product ---")
# Rename the column for cleaner output
revenue_by_product.columns = ['Product', 'TotalRevenue']
print(revenue_by_product.to_string(index=False))
print("\n")

# Calculate and print the average units sold across all data
average_units = df['UnitsSold'].mean()
print(f"📊 Average Units Sold per entry: {average_units:.1f} units")
