-- 6. sales_agent_invoices.sql: Provide a query that shows the invoices associated with each sales agent. The resultant table should include the Sales Agent's full name.

SELECT Employee.FirstName || " " || Employee.LastName AS "Sales Agent", Invoice.InvoiceId
FROM Customer, Invoice, Employee
WHERE Employee.EmployeeId=Customer.SupportRepId