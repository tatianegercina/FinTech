CREATE TABLE departments (
  id integer(11) UNIQUE NOT NULL,
  dept_name VARCHAR (255) NOT NULL,
  primary key (id)
);

CREATE TABLE employees (
  employee_id INTEGER(11) UNIQUE NOT NULL,
  first_name VARCHAR (255) NOT NULL,
  last_name VARCHAR (255) NOT NULL,
  department_id INTEGER (11) NOT NULL,
  PRIMARY KEY (employee_id),
  FOREIGN KEY (department_id) REFERENCES departments(id)
);


INSERT INTO departments (id, dept_name) VALUES (25, "data");
INSERT INTO departments (id, dept_name) VALUES (45, "webdev");

INSERT INTO employees (employee_id, first_name, last_name, department_id) VALUES (3, "Chris", "Christian", 25);
INSERT INTO employees (employee_id, first_name, last_name, department_id) VALUES (14, "Jan", "Jansson", 45);
INSERT INTO employees (employee_id, first_name, last_name, department_id) VALUES (17, "Sam", "Samuels", 45);


SELECT * FROM employees e
JOIN departments d
ON (e.department_id = d.id)
WHERE e.department_id = 45;
