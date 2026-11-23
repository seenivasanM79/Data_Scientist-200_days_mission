-- Creating Table

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


-- 1. Calculate the total spending for each city.

SELECT City, sum(Spending) AS Total_Spending From Customers
GROUP BY City ;


-- 2. Calculate the average spending for each city.

SELECT City, AVG(Spending) AS Average_Spending From Customers
GROUP BY City ;


-- 3. Count the number of customers in each city.

SELECT City,COUNT(*) AS No_of_Customers From Customers
GROUP BY City ;


-- 4. Find the maximum spending in each city.

SELECT City,MAX(Spending) AS Highest_Spending From Customers
GROUP BY City ;


-- 5.. Display each city's total spending in descending order.

SELECT City,SUM(Spending) AS Total_Spending From Customers
GROUP BY City 
ORDER BY SUM(Spending) DESC;


-- 6. Display only cities having more than two customers.

SELECT City,COUNT(*) AS No_of_Customers From Customers
GROUP BY City 
HAVING COUNT(*) > 2 ;


-- 7. Display cities where total spending exceeds ₹50,000.

SELECT City,SUM(Spending) AS Total_Spending From Customers
GROUP BY City 
HAVING SUM(Spending) > 50000 ;


-- 8. Display cities where average spending exceeds ₹30,000.

SELECT City,AVG(Spending) AS Average_Spending From Customers
GROUP BY City 
HAVING AVG(Spending) > 30000 ;


-- 9. Count customers in each city whose age is above 25.

SELECT City,COUNT(*) AS No_of_Customers From Customers
WHERE Age > 25
GROUP BY City ;


/* 10. Display cities having at least two customers, along with their total and average spending. 
Sort by total spending from highest to lowest. */

SELECT City,COUNT(*) AS No_of_Customers,
SUM(Spending) AS Total_Spending,
AVG(Spending) AS Average_Spending 
From Customers
GROUP BY City
HAVING COUNT(*) >= 2
ORDER BY SUM(Spending) DESC ;


/* Placement drill
Business scenario:

An e-commerce company wants to identify its best-performing cities.

Generate a report showing:
- City name
- Number of customers
- Total spending
- Average spending
Only include cities that:
- Have at least two customers.
- Have total spending greater than ₹50,000.
Sort the results by total spending in descending order.

Write this as a single SQL query. */

SELECT City,
COUNT(*) AS No_of_Customers,
SUM(Spending) AS Total_Spending,
AVG(Spending) AS Average_Spending 
From Customers
GROUP BY City
HAVING COUNT(*) >= 2 and SUM(Spending) > 50000
ORDER BY SUM(Spending) DESC ;