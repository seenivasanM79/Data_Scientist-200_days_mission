from datetime import datetime
from datetime import time
from datetime import date

#Task_1_Today's Date

print("Today's Date: ", date.today())
print("Current time: ", datetime.now().strftime("%H:%M:%S"))
print("Current Year: ",date.today().year)

#Task_2 - Days between Dates

start= date(2026, 8, 1)
end= date(2026, 12, 31)

print("\nDays between dates: ",end - start,"\n")

#Task_3 Employee Joining report

employees = [
    {"name": "Rahul", "joining_date": "2022-06-15"},
    {"name": "Priya", "joining_date": "2021-11-20"},
    {"name": "Arun", "joining_date": "2024-01-10"}
]

today= datetime.today()

for employee in employees:
    joining_date= datetime.strptime(employee["joining_date"], "%Y-%m-%d")

    days_worked= (today- joining_date).days
    years_worked= days_worked/ 365

    print(employee["name"], "- ", format(years_worked, ".1f"), "years.")
          
#Task_4 - Mini data Processing
sales = [
    {"date": "2026-07-28", "amount": 1200},
    {"date": "2026-07-29", "amount": 1500},
    {"date": "2026-07-29", "amount": 1800},
    {"date": "2026-07-30", "amount": 900},
    {"date": "2026-07-30", "amount": 2100}
]

daily_sales= {}

for sale in sales:
    date= sale["date"]
    amount= sale["amount"]
    if date in daily_sales:
        daily_sales[date] += amount
    else :
        daily_sales[date]= amount

print(daily_sales,"\n")

#Placement_Drill
departments = [
    "HR",
    "IT",
    "HR",
    "Finance",
    "IT",
    "IT"
]

count= {}

for department in departments:
    if department in count:
        count[department] += 1
    else:
        count[department] = 1

print(count)
