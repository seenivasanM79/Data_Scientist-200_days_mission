#TASK_1
nums = [12,7,18,22,9]

#print all numbers using loop
for i in nums:
    print(i, end= " ")


#print only even numbers
print("\n")
for j in nums:
    if j%2==0 :
        print(j, end = " ")


#Create a new list with squares of numbers
print("\n")
squared = []

for k in nums:
    squared.append(k**2)
print(squared)

#TASK_2
def  sum_list(lst):
    tot = 0
    for l in lst:
        tot += l
    return tot
print("Sum of the list:", sum_list(nums))

def max_list(lst):
    maxi = lst[0]
    for m in lst:
        if m > maxi :
            maxi = m
    return maxi

print("Maximum value: ",max_list(nums))


def  min_list(lst):
    mini= lst[0]
    for n in lst:
        if mini > n :
            mini = n
    return mini

print("Minimum value:",min_list(nums))

 #TASK 3 - Data Cleaning Simulation

data = [10, None, 25, None, 30, 5, None]
cleaned_data = []

for o in data :
    if o is not None : # if isinstance(o, int) : this can also be used and its recommended
          cleaned_data.append(o)
print(cleaned_data)
#In review its been said that here my job is to remove none so
#just for o is not None is enough here

def average_data(cd):
    if len(cd) == 0:
        return None
    tot = 0
    for p in cd:
        tot += p
    avg = tot/len(cd)
    return avg
print("Average value of cleaned data:", average_data(cleaned_data))

        
        
        
    
