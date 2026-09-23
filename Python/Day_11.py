#Task_1 - Safe Division

def safe_divide(a, b):
    try :
        c = a/b
    except ZeroDivisionError :
        print("Cannot divide by zero")
    else :
        print("The solution is: ", c)
    finally :
        print("Execution completed.\n")
        
safe_divide(5,0)
safe_divide(10,2)

#Task_2 - Validate User Input

def get_age():
    try :
        age= int(input("Enter your age: "))
    except ValueError :
        print("Invalid value, Enter your valid age.\n")
        get_age()
    else :
        print("Age accepted.\n")

get_age()
        
#Task_3 - Salary Analyzer
salary = [
    35000,
    45000,
    "abc",
    50000,
    None,
    60000
]

cleaned_salary= []
for i in salary:
    if isinstance(i, int) :
        cleaned_salary.append(i)
       
print(cleaned_salary)
print("Average salary: ",sum(cleaned_salary)/ len(cleaned_salary))


""" Task_4 - Custom Exception Thinking

1. Why is exception handling important in Data Science?

Exception handling is important in Data Science because it prevents a program from crashing when unexpected errors occur. Data Science projects often work with large datasets
that may contain missing values, incorrect data types, or invalid inputs. By handling exceptions, we can identify errors, display meaningful messages, and allow the program to
continue running or fail gracefully. This makes data processing and machine learning applications more reliable and robust.

2. What's the difference between if checking and try-except?
if Checking	                                                                           
Used to check conditions before performing an operation.
Prevents predictable errors.	                                                                     
Example: Checking if a list is empty before accessing an element.	
try-except
        Used to catch and handle unexpected errors that occur during execution.
        Handles unpredictable runtime errors.
        Example: Handling a ZeroDivisionError or FileNotFoundError.

3. Give three real situations where exception handling is useful.
Reading a dataset
If the CSV file does not exist, a FileNotFoundError can be handled without crashing the program.
User input
If a user enters text instead of a number, a ValueError can be caught and the user can be asked to enter a valid number.
Machine Learning model prediction
If the input data has the wrong shape or missing features, the program can catch the error and display a helpful message instead of stopping unexpectedly. """

# Bonus challenge
class Account :
    total_balance= 0
    def deposit(amt):
        total_balance+= amt
        return f"Rs. {amt} received and the total balance available is Rs.{total_balance}."

    def withdraw(amt):
        try :
            total_amount= total_amount - amt
        except amt> total_amount


    def show_balance():

# i don't know this

# i did that max problem already and i already know about those formulas in excel.

        
