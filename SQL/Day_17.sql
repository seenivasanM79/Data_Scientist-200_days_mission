-- Creating Customer table

CREATE TABLE Customers(
  Name Varchar(20),
  City Varchar(15),
  Age INT,
  Spending INT
);



-- Inserting Values
INSERT INTO Customers (Name, City, Age, Spending)
VALUES
('Arun', 'Chennai', 22, 15000),
('Priya', 'Mumbai', 27, 25000),
('Rahul', 'Chennai', 31, 40000),
('Anitha', 'Bangalore', 24, 18000),
('Vijay', 'Mumbai', 29, 32000),
('Aravind', 'Chennai', 35, 50000),
('Priyanka', 'Delhi', 26, 27000),
('Karthik', 'Bangalore', 30, 45000);

-- 1. Display all customers sorted by age in ascending order.

SELECT * FROM Customers
ORDER BY Age ASC ;

-- 2. Display all customers sorted by spending in descending order.

SELECT * FROM Customers
ORDER BY Spending DESC ;

-- 3. Display the top 3 highest-spending customers.

SELECT * FROM Customers
ORDER BY Spending DESC LIMIT 3;

-- 4. Display the 2 youngest customers.

SELECT * FROM Customers
ORDER BY Age ASC LIMIT 2;

-- 5. Display the 3 customers with the lowest spending.

SELECT * FROM Customers
ORDER BY Spending ASC LIMIT 3;

-- 6. Display only the names and spending of the top 4 customers by spending.

SELECT Name, Spending FROM Customers
ORDER BY Spending DESC LIMIT 4;

-- 7. Display customers sorted by city alphabetically, then by spending from highest to lowest within each city.

SELECT * FROM Customers
ORDER BY City, Spending DESC;


-- 8. Display the top 3 highest-spending customers from Chennai only.

SELECT * FROM Customers where City = "Chennai"
ORDER BY Spending DESC LIMIT 3;


--Placement drill
-- Business scenario: An e-commerce company wants to identify its two highest-value customers from Mumbai.

SELECT Name, Spending FROM Customers
where City = "Mumbai"
Order by Spending DESC Limit 2;
