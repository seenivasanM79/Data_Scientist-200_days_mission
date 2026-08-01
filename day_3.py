def add(a,b):
    print("Addition of a and b :",a+b)
add(5,7)

def is_even(n):
    if n%2 ==0:
        print(n, " is a even number")
    else:
         print(n, " is a odd number")

is_even(52)
is_even(33)

def maxi(n1,n2,n3):
    if n1>= n2 and n1>=n3:
        print(n1, " is the largest number.")
    elif n2>=n1 and n2>=n3:
        print(n2, " is the largest number.")
    else :
        print(n3, " is the largest number.")

maxi(34,66,12)

def is_leapyear(year):
    if (year%4 == 0 and year%100 != 0) or (year%400 ==0):
        return year," is leap year."
    else :
        return year," is not a leap year."
print(is_leapyear(2024))
print(is_leapyear(1900))
print(is_leapyear(2000))
print(is_leapyear(2023))

def is_prime(num):
    if num<=1 :
        return num ," is not a prime number."
    else:
        for i in range(2,round(num*0.5)+1):
            if num%i == 0:
                return num, " is not a prime number."
        else :
            return num ," is a prime number."
        
print(is_prime(-6))
print(is_prime(2))
print(is_prime(36))
