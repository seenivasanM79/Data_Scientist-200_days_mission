CREATE TABLE Customers (
    Customer_ID INT PRIMARY KEY,
    Name VARCHAR(30),
    City VARCHAR(30),
    Age INT,
    Spending INT,
    Email VARCHAR(50)
);

INSERT INTO Customers VALUES
(1, 'Arun', 'Chennai', 22, 15000, 'arun@gmail.com');

INSERT INTO Customers VALUES
(2, 'Priya', 'Mumbai', 27, 25000, 'priya@gmail.com');

INSERT INTO Customers VALUES
(3, 'Rahul', 'Chennai', 31, 40000, NULL);

INSERT INTO Customers VALUES
(4, 'Anitha', 'Bangalore', 24, 18000, 'anitha@gmail.com');

INSERT INTO Customers VALUES
(5, 'Vijay', 'Mumbai', 29, 32000, NULL);

INSERT INTO Customers VALUES
(6, 'Aravind', 'Chennai', 35, 50000, 'aravind@gmail.com');

INSERT INTO Customers VALUES
(7, 'Priyanka', 'Delhi', 26, 27000, 'priyanka@gmail.com');

INSERT INTO Customers VALUES
(8, 'Karthik', 'Bangalore', 30, 45000, 'karthik@gmail.com');

--Task_1
-- All unique cities.
SELECT DISTINCT City from Customers ;

-- All unique customer ages.
SELECT DISTINCT Age from Customers;

--Task_2
--Find customers whose name starts with A.
Select Name from Customers Where Name LIKE "A%";

--Find customers whose name ends with a.
Select Name from Customers Where Name LIKE "%a";

--Find customers whose name contains an.
Select Name from Customers where Name Like "%an%";

--Task_3
--Find customers from Chennai or Mumbai.
Select Name from Customers where City IN ("Chennai", "Mumbai");

--Find customers from Delhi, Mumbai, or Bangalore.
select Name from Customers Where City In ("Delhi", "Mumbai", "Bangalore");

--Task_4
--Find customers whose spending is between 20,000 and 40,000.
Select * from Customers Where Spending Between 20000 and 40000;

--Find customers whose age is between 25 and 30.
Select * from Customers where age between 25 and 30;

--Task-5
--Find customers whose email is missing.
Select * from Customers where Email is Null;

--Find customers whose email is available.
Select * from Customers where Email is not NULL;

--Placement Drill
--Give me the names and spending amounts of customers from Chennai or Mumbai who are between 25 and 35 years old and have spent at least ₹25,000.
Select Name, Spending from Customers 
Where City in ("Chennai", "Mumbai") and 
Spending >= 25000 and 
Age between 25 and 35;