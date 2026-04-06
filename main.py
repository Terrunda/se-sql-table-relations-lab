# STEP 0

# SQL Library and Pandas Library
import sqlite3
import pandas as pd

# Connect to the database
conn = sqlite3.connect('data.sqlite')

pd.read_sql("""SELECT * FROM sqlite_master""", conn)

# STEP 1
# Replace None with your code
df_boston = "SELECT firstName, lastName, jobTitle FROM employees WHERE officeCode = '2'"

# Replace None with your code
df_zero_emp = "SELECT * FROM employees WHERE officeCode NOT IN (SELECT DISTINCT officeCode FROM employees)"

# STEP 3
# Replace None with your code
df_employee = "SELECT e.firstName, e.lastName, o.city, o.state FROM employees e LEFT JOIN offices o ON e.officeCode = o.officeCode ORDER BY e.firstName, e.lastName"

# STEP 4
# Replace None with your code
df_contacts = "SELECT contactFirstName, contactLastName, phone, salesRepEmployeeNumber FROM customers c LEFT JOIN orders o ON c.customerNumber = o.customerNumber WHERE o.orderNumber IS NULL ORDER BY contactLastName ASC;"

# STEP 5
# Replace None with your code
df_payment = """
SELECT 
    c.contactFirstName, 
    c.contactLastName, 
    p.paymentDate, 
    p.amount
FROM customers c
JOIN payments p ON c.customerNumber = p.customerNumber;
"""

# STEP 6
# Replace None with your code
df_credit = """
SELECT 
    e.employeeNumber, 
    e.firstName, 
    e.lastName, 
    COUNT(c.customerNumber) AS numberOfCustomers
FROM employees e
JOIN customers c ON e.employeeNumber = c.salesRepEmployeeNumber
GROUP BY e.employeeNumber, e.firstName, e.lastName
HAVING AVG(c.creditLimit) > 90000
ORDER BY numberOfCustomers DESC;
"""

# STEP 7
# Replace None with your code
df_product_sold = """
SELECT 
    p.productName, 
    COUNT(od.orderNumber) AS numorders, 
    SUM(od.quantityOrdered) AS totalunits
FROM products p
JOIN orderdetails od ON p.productCode = od.productCode
GROUP BY p.productName
ORDER BY totalunits DESC;
"""

# STEP 8
# Replace None with your code
df_total_customers ="""
SELECT 
    p.productName, 
    p.productCode, 
    COUNT(DISTINCT o.customerNumber) AS numpurchasers
FROM products p
JOIN orderdetails od ON p.productCode = od.productCode
JOIN orders o ON od.orderNumber = o.orderNumber
GROUP BY p.productName, p.productCode
ORDER BY numpurchasers DESC;
"""

# STEP 9
# Replace None with your code
df_customers = """
SELECT 
    o.officeCode, 
    o.city, 
    COUNT(c.customerNumber) AS n_customers
FROM offices o
LEFT JOIN employees e ON o.officeCode = e.officeCode
LEFT JOIN customers c ON e.employeeNumber = c.salesRepEmployeeNumber
GROUP BY o.officeCode, o.city
ORDER BY n_customers DESC;"""

# STEP 10
# Replace None with your code
df_under_20 = """
SELECT DISTINCT 
    e.employeeNumber, 
    e.firstName, 
    e.lastName, 
    off.city, 
    off.officeCode,
    od.productCode
FROM employees e
JOIN offices off ON e.officeCode = off.officeCode
JOIN customers c ON e.employeeNumber = c.salesRepEmployeeNumber
JOIN orders o ON c.customerNumber = o.customerNumber
JOIN orderdetails od ON o.orderNumber = od.orderNumber
"""

conn.close()