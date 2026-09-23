#Day_9

#Task_1 - File created

#Task_2 Read and Diaplay

import csv
filename ="employees.csv"

with open(filename, "r") as csvfile :
    csvreader = csv.reader(csvfile)
    for line in csvreader:
        print(line)
 
#Task_3 - Calculate Average salary

import pandas as pd
df = pd.read_csv(filename)
print("\n",df)
avg_salary = df["Salary"].mean()
print("\nAverage Salary: ",avg_salary)

#Task_4 - Count Employees by Department

Emp_dept = {
    }
for i in df["Department"] :
    if i not in Emp_dept :
        Emp_dept[i] = 1
    else :
        Emp_dept[i] +=1

print("\nEmployees by Department: \n",Emp_dept)

# Task_5 - Highest Salary

print("\nEmployee with Max Salary") 
print("Name: ", df.loc[df["Salary"].idxmax(), "Name"],"\nSalary: ",df["Salary"].max())

