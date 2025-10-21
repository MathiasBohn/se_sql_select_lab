# STEP 1A
# Import SQL Library and Pandas
import sqlite3
import pandas as pd

# STEP 1B
# Connect to the database
conn = sqlite3.connect('data.sqlite')

# Optional: View the employees table to understand the data
employee_data = pd.read_sql("""SELECT * FROM employees""", conn)
print("---------------------Employee Data---------------------")
print(employee_data)
print("-------------------End Employee Data-------------------")
print()

# STEP 2
# Get employee number and last name from all employees
df_first_five = pd.read_sql("""
SELECT employeeNumber, lastName 
FROM employees
""", conn)
print("---------------------Step 2 Results---------------------")
print(df_first_five)
print()

# STEP 3
# Same as Step 2 but with last name first, then employee number
df_five_reverse = pd.read_sql("""
SELECT lastName, employeeNumber 
FROM employees
""", conn)
print("---------------------Step 3 Results---------------------")
print(df_five_reverse)
print()

# STEP 4
# Same as Step 3 but rename employeeNumber column to 'ID' using alias
df_alias = pd.read_sql("""
SELECT lastName, employeeNumber AS ID 
FROM employees
""", conn)
print("---------------------Step 4 Results---------------------")
print(df_alias)
print()

# STEP 5
# Use CASE to classify employees as "Executive" or "Not Executive"
df_executive = pd.read_sql("""
SELECT *,
    CASE 
        WHEN jobTitle = "President" OR jobTitle = "VP Sales" OR jobTitle = "VP Marketing" THEN "Executive"
        ELSE "Not Executive"
    END AS role
FROM employees
""", conn)
print("---------------------Step 5 Results---------------------")
print(df_executive[['firstName', 'lastName', 'jobTitle', 'role']])
print()

# STEP 6
# Find the length of each employee's last name
df_name_length = pd.read_sql("""
SELECT LENGTH(lastName) AS name_length
FROM employees
""", conn)
print("---------------------Step 6 Results---------------------")
print(df_name_length)
print()

# STEP 7
# Get the first two letters of each job title
df_short_title = pd.read_sql("""
SELECT SUBSTR(jobTitle, 1, 2) AS short_title
FROM employees
""", conn)
print("---------------------Step 7 Results---------------------")
print(df_short_title)
print()

# Optional: View the orderDetails table
order_details = pd.read_sql("""SELECT * FROM orderDetails""", conn)
print("------------------Order Details Data------------------")
print(order_details)
print("----------------End Order Details Data----------------")
print()

# STEP 8
# Calculate the sum of all rounded total prices (priceEach * quantityOrdered)
sum_total_price = pd.read_sql("""
SELECT SUM(ROUND(priceEach * quantityOrdered)) AS total
FROM orderDetails
""", conn)['total']
print("---------------------Step 8 Results---------------------")
print(f"Sum of total prices: ${sum_total_price[0]:,.2f}")
print()

# STEP 9
# Extract day, month, and year from orderDate in Day/Month/Year format
# Note: orderDate is in the 'orders' table, not 'orderDetails'
df_day_month_year = pd.read_sql("""
SELECT orderDate,
    STRFTIME('%d', orderDate) AS day,
    STRFTIME('%m', orderDate) AS month,
    STRFTIME('%Y', orderDate) AS year
FROM orders
""", conn)
print("---------------------Step 9 Results---------------------")
print(df_day_month_year.head(10))
print()

# Close the connection
conn.close()
print("Database connection closed successfully!")