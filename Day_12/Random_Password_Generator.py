import random
import string

nums= [ str(i) for i  in range(10) ]
i1= random.choices(nums,k=2)
i2=  random.choices(nums,k=2)

lower = list(string.ascii_lowercase)
upper = list(string.ascii_uppercase)

l= random.choices(lower, k=2)
u= random.choices(upper, k=2)

combined_list = i1 + l + i2 + u
password= "".join(combined_list)

print("Password: ", password)
