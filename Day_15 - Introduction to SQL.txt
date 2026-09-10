#CREATING TABLE EMPLOYEES :

CREATE TABLE Employees(
Employee_ID int PRIMARY KEY,
Name Varchar(25),
Department Varchar(20),
Salary int,
Age int
);


#INSERTING VALUES :

INSERT INTO Employees VALUES(1,"Rahul", "IT", 50000, 24);
INSERT INTO Employees VALUES(2, "Priya", "HR", 45000, 26);
INSERT INTO Employees VALUES(3, "Arun", "IT", 60000, 28);
INSERT INTO Employees VALUES(4, "Sneha", "Finance", 70000, 30);
INSERT INTO Employees VALUES(5, "Vijay", "HR", 42000, 25);

✅ Task 1

Write SQL queries to:

A)

Display all columns.

B)

Display only:

Name
Salary
C)

Display employees whose salary is greater than 50000.

D)

Display employees whose department is HR.

E)

Display employees ordered by salary from highest to lowest.

# TASK_1 SOLUTIONS:

SELECT * FROM Employees;

SELECT Name, Salary FROM Employees;

SELECT * FROM Employees WHERE Salary > 50000;

SELECT * FROM Employees WHERE Department = "HR";

SELECT * FROM Employees ORDER BY Salary DESC ;


✅ Task 2

Using the same table, write SQL queries for:

A)

Employees whose age is greater than 25.

B)

Employees in the IT department with salary greater than 55000.

C)

Employees who are not in HR.

(Hint: != or <>)

D)

Display only the Department column.

#TASK_2 SOLUTIONS:

SELECT * FROM Employees WHERE Age > 25;

SELECT * FROM Employees WHERE Department = "IT" AND Salary > 55000;

SELECT * FROM Employees WHERE Department != "HR";

SELECT Department FROM Employees;