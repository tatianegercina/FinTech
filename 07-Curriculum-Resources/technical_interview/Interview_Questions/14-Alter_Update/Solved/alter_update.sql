-- MySQL
ALTER TABLE employees
CHANGE department_id dept_id VARCHAR(255);

ALTER TABLE employees
ADD annual_salary INT(11);

UPDATE employees
SET annual_salary = 80000
WHERE employee_id = 17;
