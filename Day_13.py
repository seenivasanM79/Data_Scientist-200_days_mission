#Task_1

numbers= [3, 7, 10, 15, 20, 25]

squares= [i**2 for i in numbers]
print("Squares: ",squares)

even= [j for j in numbers if j%2== 0]
print("Even: ",even)

above= [k for k in numbers if k>10]
print("Values greater than 10: ",above)


#Task_2
numberss= [1, 2, 3, 4, 5]

squared_dict= {l: l **2 for l in numberss }
print("Dictionary of Squared numbers: ", squared_dict)



#Task_3
square= lambda y : y**2
print(square(6))

add= lambda a,b : a+b
print(add(3,5))

iseven= lambda z : ["True" if z%2==0 else "False"]
print(iseven(6))


#Task_4
data= [12, None, 8, None, 25, 30, None, 5]

cleaned_data= [m for m in data if m is not None]
print("Cleaned_data: ",cleaned_data)
print("Total: ", sum(cleaned_data))
print("Average: ", sum(cleaned_data)/len(cleaned_data))

