-- 3. brazil_customers_invoices.sql: Provide a query showing the Invoices of customers who are from Brazil. The resultant table should show the customer's full name, Invoice ID, Date of the invoice and billing country.

SELECT cust.FirstName, cust.LastName, inv.InvoiceId, inv.InvoiceDate, inv.BillingCountry
FROM Customer as cust
JOIN Invoice as inv ON inv.CustomerId=cust.CustomerId
WHERE cust.Country='Brazil'