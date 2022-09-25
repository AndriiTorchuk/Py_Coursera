SELECT
EmployeeId, FirstName, LastName
FROM
Employee
JOIN 
(SELECT EmployeeId, SUM(Value) as Total
FROM
Payments
GROUP BY EmployeeId) sm
ON sm.EmployeeId = em.EmployeeId