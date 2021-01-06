# Write your MySQL query statement below

SELECT Department.Name AS Department, Employee.Name AS Employee, Salary
FROM Employee
INNER JOIN Department 
ON Employee.DepartmentId=Department.Id 
WHERE (DepartmentId, Salary) 
IN (SELECT DepartmentId, MAX(Salary)
FROM Employee
GROUP BY DepartmentId)