#Basic variable declaration
name = "seeni"
age = 19
height = 173.00
is_student = True

lst = [1,2,3,4,5]
dict = {'maths':79, 'Science':83}

print(dict)

#Basic operations
add = 2 + 3
print(add)

greet = "Hello " + name
print(greet)

print(lst[0:3])

#Input/Output

name = input("Enter your name :")
num = int(input("Enter your Favourite number :"))
print(name ,"'s Favourite number is", num)

#Conditional statement
if age > 18:
    print("Adult")
else:
    print("Minor")

#write a program to find a number is even or odd
if num%2 == 0:
    print(num, " is even number")
else :
    print(num, " is Odd number")

#Print max, min, sum of a list
print("Sum", sum(lst))
print("Min", min(lst))
print("Max", max(lst))

#Write a program to reverse a string
str = "Programming"
print(str[::-1])
