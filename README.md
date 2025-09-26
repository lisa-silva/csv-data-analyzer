Python CSV Data Analyzer (Pandas)
📊 Project Overview

This is a demonstration of data loading, cleaning, and analysis using the industry-standard Pandas library in Python.

The script, data_analyzer.py, processes a sample sales dataset (sales_data.csv) and generates a summary report detailing total revenue, high-performance sales, and revenue breakdown by product.
🛠️ Skills Demonstrated

This project showcases critical data science and programming skills:

    Data Manipulation with Pandas: Successfully reading and processing data using the DataFrame structure.

    File Handling (I/O): Correctly loading external .csv files into a Python environment.

    Data Aggregation: Using the .sum() and .mean() methods to calculate summary statistics.

    Data Filtering: Applying conditional logic (df['UnitsSold'] > 100) to isolate specific data points.

    Control Flow & Error Handling: Using try...except to ensure the script handles missing files gracefully.

🚀 How to Run the Script
1. Installation

This project requires the Pandas library:

pip install pandas

2. Execution

    Ensure both data_analyzer.py and sales_data.csv are in the same directory.

    Run the script from your terminal:

python data_analyzer.py

Expected Output Example

--- Total Summary ---
💰 Grand Total Revenue: $317,000.00
...
--- Revenue Breakdown by Product ---
Product  TotalRevenue
 Laptop        207000
Monitor        110000

