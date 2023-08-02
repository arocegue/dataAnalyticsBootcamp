SELECT employees.emp_no, employees.last_name, employees.first_name, employees.sex, salaries.salary
FROM employees, salaries
WHERE employees.emp_no = salaries.emp_no

SELECT employees.first_name, employees.last_name, employees.hire_date
FROM employees
WHERE date_part('year', employees.hire_date) = '1986'

SELECT d.dept_no, d.dept_name, e.emp_no, e.last_name, e.first_name
FROM departments AS d, dept_manager AS dm
LEFT JOIN (SELECT e.emp_no, e.last_name, e.first_name  FROM employees AS e) AS e
ON dm.emp_no = e.emp_no
WHERE dm.dept_no = d.dept_no

SELECT d.dept_no, e.emp_no, e.last_name, e.first_name, d.dept_name
FROM departments AS d, dept_emp AS de
LEFT JOIN (SELECT e.emp_no, e.last_name, e.first_name  FROM employees AS e) AS e
ON de.emp_no = e.emp_no
WHERE de.dept_no = d.dept_no

SELECT e.first_name, e.last_name, e.sex
FROM employees AS e
WHERE e.first_name = 'Hercules'
AND e.last_name LIKE 'B%'

SELECT e.emp_no, e.last_name, e.first_name
FROM employees AS e
INNER JOIN (
	SELECT dept_emp.emp_no
	FROM dept_emp, departments
	WHERE departments.dept_name = 'Sales'
	AND departments.dept_no = dept_emp.dept_no
) AS all_emp
ON e.emp_no = all_emp.emp_no

SELECT e.emp_no, e.last_name, e.first_name, all_emp.dept_name
FROM employees AS e
INNER JOIN (
	SELECT dept_emp.emp_no, departments.dept_name
	FROM dept_emp, departments
	WHERE (departments.dept_name = 'Sales' OR departments.dept_name = 'Development')
	AND departments.dept_no = dept_emp.dept_no
) AS all_emp
ON e.emp_no = all_emp.emp_no

SELECT COUNT(e.last_name) AS "Last Name Frequency Count", e.last_name AS "Last Name"
FROM employees AS e
GROUP BY e.last_name
ORDER BY COUNT(e.last_name) DESC