#Number Grading
mark = int(input("Enter your marks:"))

if mark >= 90 :
    print("You got A grade !!!")
elif 75 <= mark <= 89 :
    print("You got B grade !!")
elif 60<= mark <= 74:
    print("You got C grade !")
else :
    print("You falied :(")
    
#Leap year checker
year = int(input("Enter the year:"))

if (year%4 == 0 and year%100 != 0) and (year%400 ==0):
    print(year, " is a leap year")
else :
     print(year, " is not a leap year")

#print pattern
pat = "*"
for i in range(1,6):
    print(pat*i)
    
#Sum of digits
number = int(input("Enter a number: "))

sum = 0
while number > 0:
    sum += number % 10
    number //= 10
    

print("Sum of digits is ", sum)

#Prime number checker
number = int(input("Enter a number to check whether it is prime or not:"))

if number <= 1:
    print("Not a prime number")
else:
    for k in range(2, number):
        if number % k == 0:
            print("Not a prime number")
            break
    else:
        print("Prime number")
