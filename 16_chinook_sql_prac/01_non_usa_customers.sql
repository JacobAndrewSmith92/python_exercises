-- 1. non_usa_customers.sql: Provide a query showing Customers (just their full names, customer ID and country) who are not in the US.

SELECT cust.FirstName, cust.LastName, cust.CustomerId, cust.Country
FROM Customer as cust
WHERE cust.Country!='USA'
