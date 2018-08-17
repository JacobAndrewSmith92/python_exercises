-- 2. brazil_customers.sql: Provide a query only showing the Customers from Brazil.

SELECT cust.FirstName, cust.LastName, cust.CustomerId, cust.City, cust.Country
FROM Customer as cust
WHERE cust.Country='Brazil'