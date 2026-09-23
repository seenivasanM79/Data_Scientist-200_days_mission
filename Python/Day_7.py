#DAY-7

#Task_1 - Dictionary Basics

student = { "name" : "Seenivasan",
            "age" : 19,
            "department" : "Data Science",
            "cgpa" : 8.5
            }

#Print the entire dictionary
print(student)

#print only name
print("\n",student["name"])

#print only the cgpa
print("\n",student["cgpa"])

print("Alterating Dictionary")
#Adding new key
student["city"] = "chennai"
print("\n",student)

#Changing cgpa value
student["cgpa"] = 8.6

del student["city"]
print("\n",student)


#Task_2 - Frequency counter

fruits = [
    "apple",
    "banana",
    "apple",
    "orange",
    "banana",
    "apple"
]
print("\n",fruits)
d_fruits = { "apple" : 0, "banana" : 0, "orange" : 0}
for i in fruits :
    for j in d_fruits :
        if i in j :
            d_fruits[j] += 1

print("Frequency Counter",d_fruits)
     

#Task_3 - Character Frequency


text = "data science"
print("\n",text)
text = text.lower()
cf = {}
for k in text :
    if k in cf:
        cf[k] += 1
    else :
        cf[k] = 1

print("Character Frequency :",cf)


