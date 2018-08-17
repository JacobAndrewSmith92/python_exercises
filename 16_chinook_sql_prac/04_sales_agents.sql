-- 4. sales_agents.sql: Provide a query showing only the Employees who are Sales Agents.

SELECT emp.EmployeeId, emp.FirstName, emp.LastName, emp.Title, emp.Country
FROM Employee as emp
WHERE emp.Title='Sales Support Agent'