-- ALTER TABLE

-- 1
ALTER TABLE job_history 
ADD INDEX indx_job_id(job_id);

-- 2
ALTER TABLE job_history
DROP INDEX indx_job_id;

-- 3
ALTER TABLE locations
ADD region_id  INT;

-- 4
ALTER TABLE locations
DROP city;

-- 5
ALTER TABLE locations
MODIFY country_id INT;

-- 6
ALTER TABLE locations
CHANGE state_province state varchar(25);

-- 7
ALTER TABLE locations
DROP PRIMARY KEY,
ADD PRIMARY KEY(location_id,country_id);

-- 8
ALTER TABLE locations
DROP PRIMARY KEY;

-- 9
ALTER TABLE job_history
ADD FOREIGN KEY(job_id)
REFERENCES jobs(job_id);

-- 10
ALTER TABLE job_history
DROP FOREIGN KEY fk_job_id;




-- INSERT INTO

-- 1
INSERT INTO countries (country_id,country_name)
VALUES (1,'España'), (2, 'Alemania'), (3, 'Francia');

-- 2
CREATE TEMPORARY TABLE country_new 
AS (SELECT *
FROM countries);

-- 3
INSERT INTO countries VALUES(4, 'Suecia', 11827), (5, 'Grecia', 11830), (6, 'Nueva Zelanda', 11826);

-- 4
INSERT INTO country_new
SELECT * FROM countries;



-- UPDATE

-- 1
UPDATE employees
SET email = 'not available', commission_pct = 0.10
WHERE department_id = 110;

-- 2
UPDATE employees 
SET email = 'not available'
WHERE department_id = (
SELECT department_id 
FROM departments 
WHERE department_name = 'Accounting');

-- 3
UPDATE employees
SET JOB_ID = 'SH_CLERK' 
WHERE employee_id = 118 
AND department_id = 30 
AND JOB_ID NOT LIKE 'SH%';

-- 4
UPDATE employees 
SET email = 'not available'
WHERE department_id = 80 AND commission_pct < 0.2;



-- SELECT

-- 1
SELECT first_name AS "Nombre", last_name AS "Apellido"
FROM employees;

-- 2
SELECT DISTINCT department_id AS "ID DEPARTAMENTO"
FROM employees;

-- 3
SELECT *
FROM employees
ORDER BY first_name DESC;

-- 4
SELECT CONCAT(first_name, last_name) AS "Nombre completo"
FROM employees;

-- 5
SELECT job_id AS "ID trabajo", MAX(salary) AS "Salario máximo"
FROM employees
GROUP BY job_id
HAVING MAX(salary) >= 4000;

-- 6
SELECT CONCAT(first_name, last_name) AS "Nombre", salary AS "Salario"
FROM employees
WHERE salary NOT BETWEEN 10000 AND 15000;

-- 7
CREATE VIEW vistatest AS
SELECT CONCAT(first_name, last_name ) AS "Nombre", department_id AS "ID departamento"
FROM employees
WHERE department_id IN (30, 100)
ORDER BY department_id ASC;

SELECT * FROM vistatest;
UPDATE vistatest
SET department_id = 31 
WHERE department_id = 30;

-- 8
CREATE VIEW vistatest2 AS
SELECT CONCAT(first_name, last_name ) AS "Nombre", salary AS "Salario"
FROM employees
WHERE salary NOT IN (10000, 15000) AND department_id = 31 OR department_id = 100;

-- 9
SELECT job_id AS "Tipo trabajo", count(job_id) AS "Número empleados"
FROM employees
GROUP BY job_id
ORDER BY count(job_id) DESC;

-- 10
SELECT MAX(salary) AS "Máximo", MIN(salary) AS "Mínimo", SUM(salary) AS "Suma", ROUND(AVG(salary), 0) AS "Promedio"
FROM employees
GROUP BY employee_id;

-- 11
SELECT manager_id AS "ID Manager", MIN(salary) AS "Salario minimo"
FROM employees
WHERE manager_id IS NOT NULL
GROUP BY manager_id
ORDER BY MIN(salary) DESC;

-- 12
SELECT job_id AS "ID trabajo", AVG(salary) AS "Promedio"
FROM employees
WHERE job_id NOT LIKE 'IT_PROG'
GROUP BY job_id;

-- 13
SELECT job_id AS "ID trabajo", SUM(salary) AS "Total", MAX(salary) AS "Máximo", MIN(salary) AS "Mínimo", AVG(salary) AS "Promedio"
FROM employees
WHERE department_id = '90'
GROUP BY job_id;

-- 14
SELECT last_name AS "Apellido"
FROM employees
WHERE CHAR_LENGTH(last_name) = 6;

-- 15
SELECT LEFT(first_name, 3) AS "Primeros 3 chars"
FROM employees;