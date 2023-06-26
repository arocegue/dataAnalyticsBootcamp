CREATE TABLE departments (
	dept_no VARCHAR(5) PRIMARY KEY UNIQUE,
	dept_name VARCHAR(50)
);


CREATE TABLE titles (
	
	title_id VARCHAR(10) PRIMARY KEY UNIQUE,
	title VARCHAR(50)
	
);

CREATE TABLE employees (
	emp_no VARCHAR(10) PRIMARY KEY UNIQUE,
	emp_title_id VARCHAR(10),
	FOREIGN KEY(emp_title_id) REFERENCES titles(title_id),
	birth_date date,
	first_name VARCHAR(50),
	last_name VARCHAR(50),
	sex VARCHAR(1),
	hire_date date
);

CREATE TABLE salaries (
	emp_no VARCHAR(10),
	FOREIGN KEY (emp_no) REFERENCES employees(emp_no),
	salary INTEGER
);

CREATE TABLE dept_emp (
	emp_no VARCHAR(10),
	FOREIGN KEY (emp_no) REFERENCES employees(emp_no),
	dept_no VARCHAR(5),
	FOREIGN KEY (dept_no) REFERENCES departments(dept_no),
	PRIMARY KEY (emp_no, dept_no)
);

CREATE TABLE dept_manager (
	dept_no VARCHAR(5),
	FOREIGN KEY (dept_no) REFERENCES departments(dept_no),
	emp_no VARCHAR(10),
	FOREIGN KEY (emp_no) REFERENCES employees(emp_no),
	PRIMARY KEY (dept_no, emp_no)
);

