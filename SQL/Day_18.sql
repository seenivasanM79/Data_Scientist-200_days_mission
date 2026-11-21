-- Creating Customer1 table

CREATE TABLE Customers1(
  Name Varchar(20),
  City Varchar(15),
  Age INT,
  Spending INT
);



-- Inserting Values
INSERT INTO Customers1 (Name, City, Age, Spending)
VALUES
('Arun', 'Chennai', 22, 15000),
('Priya', 'Mumbai', 27, 25000),
('Rahul', 'Chennai', 31, 40000),
('Anitha', 'Bangalore', 24, 18000),
('Vijay', 'Mumbai', 29, 32000),
('Aravind', 'Chennai', 35, 50000),
('Priyanka', 'Delhi', 26, 27000),
('Karthik', 'Bangalore', 30, 45000);


-- 1. Count the total number of customers.

Select COUNT(*) AS Total_Customers
From Customers1 ;

-- 2. Count the number of customers who have an email address. (Add the Email column back to your table using the Day 16 dataset.)

ALTER Table Customers1 ADD column Email Varchar(50) ;

UPDATE Customers1
SET Email = CASE Name
    WHEN 'Arun' THEN 'arun@gmail.com'
    WHEN 'Priya' THEN 'priya@gmail.com'
    WHEN 'Rahul' THEN 'rahul@gmail.com'
    WHEN 'Anitha' THEN 'anitha@gmail.com'
    WHEN 'Vijay' THEN 'vijaay@gmail.com'
    WHEN 'Aravind' THEN 'aravind@gmail.com'
    WHEN 'Priyanka' THEN 'priyanka@gmail.com'
    WHEN 'Karthik' THEN 'karthick@gmail.com'
END
WHERE Name IN (
    'Arun', 'Priya', 'Rahul', 'Anitha',
    'Vijay', 'Aravind', 'Priyanka', 'Karthik'
);

SELECT Count(Email) FROM Customers1 ;


-- 3. Calculate the total spending of all customers.

SELECT Sum(Spending) AS Total_Spending FROM Customers1 ;


-- 4. Calculate the average customer spending.

SELECT Avg(Spending) AS Average_Spending FROM Customers1 ;


-- 5. Find the highest customer spending.

SELECT Max(Spending) AS Highest_Spending FROM Customers1 ;


-- 6. Find the lowest customer spending.

SELECT Min(Spending) AS Lowest_Spending FROM Customers1 ;


-- 7. Calculate the total spending of customers from Chennai only.

SELECT Sum(Spending) AS Total_Spending_Chennai
FROM Customers1 WHERE City = 'Chennai' ;


-- 8. Calculate the average spending of customers from Mumbai.

SELECT Avg(Spending) AS Average_Spending_Mumbai
FROM Customers1 WHERE City = 'Mumbai' ;


-- 9. Find the highest spending among customers aged above 25.

SELECT Max(Spending) AS Highest_Spending_Above25
FROM Customers1 WHERE Age > 25 ;


-- 10. Display total, average, maximum and minimum spending in a single query, using meaningful column aliases.

SELECT Sum(Spending) AS Total_Spending, 
AVG(Spending) AS Average_Spending,
Max(Spending) AS Maximum_Spending,
Min(Spending) AS Minimum_Spending
FROM Customers1;

-- Placement drill
/*Business scenario:

An e-commerce company wants a quick performance report for its Chennai customers.

Generate a report containing:
- Total number of Chennai customers.
- Total spending.
- Average spending.
- Highest spending.
- Lowest spending.
Your output must contain all five metrics in a single SQL query.*/

SELECT Count(*) AS Total_Customers,
Sum(Spending) AS Total_Spending, 
AVG(Spending) AS Average_Spending,
Max(Spending) AS Maximum_Spending,
Min(Spending) AS Minimum_Spending
FROM Customers1
WHERE City = 'Chennai';