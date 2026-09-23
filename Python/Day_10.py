#Task_1

class Student :
    def __init__ (self, name, age, department, cgpa):
        self.name = name
        self.age = age
        self.department = department
        self.cgpa = cgpa
    def display(self):
        return f"Name: {self.name} \nAge: {self.age} \nDepartment: {self.department} \nCGPA: {self.cgpa}"

    def grade(self):
        if self.cgpa >= 9 :
            return "Outstanding"
        elif self.cgpa >= 8 :

            return "Excellent"
        elif self.cgpa >= 7 :
            return "Good"
        else :
            return "Needs improvement"
        
            
stud = Student("Seeni", 19, "Data science", 8.5)
print(stud.display())
print("Your Grade is :", stud.grade())

#Task_2

class Employee :
    def __init__ (self, name, salary):
        self.name = name
        self.salary = salary

    def annual_salary(self) :
        return self.salary*12

emp1 = Employee("Adam", 12000)
emp2 = Employee("Ben", 15000)
emp3 = Employee("Eve", 13000)

print(f"\n{emp1.name} earns ${emp1.annual_salary()} annually" )
print(f"{emp2.name} earns ${emp2.annual_salary()} annually" )
print(f"{emp3.name} earns ${emp3.annual_salary()} annually" )

#Task_3

class SalesReport:
    def __init__(self, sales):
        self.sales = sales

    def total_sales(self):
        return f"Total sales: {sum(self.sales)}"

    def average_sales(self):
        return f"Average sales: {sum(self.sales)/len(self.sales)}"

    def highest_sales(self):
        return f"Highest sales: {max(self.sales)}"

Sreport = SalesReport([25000, 32000, 28000, 40000])
print("\n")
print(Sreport.total_sales())
print(Sreport.average_sales())
print(Sreport.highest_sales())

#Task_4

"""1. A class is a  blueprint of the methods and objects and an object is the real world entity that holds the class
2. We use __init__() to initialize variables automatically when the class is called, its called as the constructor.
3. If we have to use the use many times then writing it in a block of function or class will be useful."""

# Bonus Challenge = Done !!!

# I'm trusting you and this study plan with my whole life ...
