# STEP 0

# SQL Library and Pandas Library
import sqlite3
import pandas as pd

# Connect to the database
conn = sqlite3.connect('data.sqlite')

pd.read_sql("""SELECT * FROM sqlite_master""", conn)

# STEP 1
# Replace None with your code
df_boston = pd.read_sql("SELECT firstName, lastName FROM employees WHERE officeCode = '2'", conn)


# Replace None with your code
df_zero_emp = pd.read_sql("SELECT * FROM employees WHERE officeCode NOT IN (SELECT DISTINCT officeCode FROM employees)", conn)


# STEP 3
# Replace None with your code
df_employee = pd.read_sql("SELECT e.firstName, e.lastName, o.city, o.state FROM employees e LEFT JOIN offices o ON e.officeCode = o.officeCode ORDER BY e.firstName, e.lastName", conn)

# STEP 4
# Replace None with your code
df_contacts = pd.read_sql("SELECT contactFirstName, contactLastName, phone, salesRepEmployeeNumber FROM customers c LEFT JOIN orders o ON c.customerNumber = o.customerNumber WHERE o.orderNumber IS NULL ORDER BY contactLastName ASC;", conn)

# STEP 5
# Replace None with your code
df_payment = pd.read_sql("""
    SELECT c.contactFirstName, c.contactLastName, p.paymentDate, p.amount 
    FROM customers c 
    JOIN payments p ON c.customerNumber = p.customerNumber 
    ORDER BY CAST(p.amount AS DECIMAL) DESC
""", conn)

# STEP 6
# Replace None with your code
df_credit = pd.read_sql("""
    SELECT e.employeeNumber, e.firstName, e.lastName, COUNT(c.customerNumber) as numberOfCustomers
    FROM employees e
    JOIN customers c ON e.employeeNumber = c.salesRepEmployeeNumber
    GROUP BY e.employeeNumber
    HAVING AVG(c.creditLimit) > 90000
    ORDER BY numberOfCustomers DESC, firstName DESC
""", conn)

# STEP 7
# Replace None with your code
df_product_sold = pd.read_sql("""
SELECT 
    p.productName, 
    COUNT(od.orderNumber) AS numorders, 
    SUM(od.quantityOrdered) AS totalunits
FROM products p
JOIN orderdetails od ON p.productCode = od.productCode
GROUP BY p.productName
ORDER BY totalunits DESC;
""", conn)

# STEP 8
# Replace None with your code
df_total_customers = pd.read_sql("""
SELECT 
    p.productName, 
    p.productCode, 
    COUNT(DISTINCT o.customerNumber) AS numpurchasers
FROM products p
JOIN orderdetails od ON p.productCode = od.productCode
JOIN orders o ON od.orderNumber = o.orderNumber
GROUP BY p.productName, p.productCode
ORDER BY numpurchasers DESC;
""", conn)

# STEP 9
# Replace None with your code
df_customers = pd.read_sql("""
    SELECT 
        o.officeCode, 
        o.city, 
        COUNT(c.customerNumber) AS n_customers
    FROM offices o
    INNER JOIN employees e ON o.officeCode = e.officeCode
    INNER JOIN customers c ON e.employeeNumber = c.salesRepEmployeeNumber
    GROUP BY o.officeCode, o.city
    ORDER BY n_customers DESC
    LIMIT 1; 
""", conn)

# STEP 10
# Replace None with your code
df_under_20 = pd.read_sql("""
    WITH Underperforming AS (
        SELECT productCode
        FROM orderdetails
        GROUP BY productCode
        HAVING COUNT(DISTINCT orderNumber) < 20
    )
    SELECT DISTINCT 
        e.employeeNumber, 
        e.firstName, 
        e.lastName, 
        off.city, 
        off.officeCode
    FROM employees e
    JOIN offices off ON e.officeCode = off.officeCode
    JOIN customers c ON e.employeeNumber = c.salesRepEmployeeNumber
    JOIN orders o ON c.customerNumber = o.customerNumber
    JOIN orderdetails od ON o.orderNumber = od.orderNumber
    WHERE od.productCode IN (SELECT productCode FROM Underperforming)
    ORDER BY e.firstName ASC;
""", conn)

conn.close()