#Day_8 File Handling

###Task-1  Create a text file - created in the name of student.txt

#Task-2 - Read the file

with open("student.txt", "r") as file :
    content = file.read()
    print(content,"\n")

#Task_3 - Count Students

try :
    with open("student.txt", "r") as file1:
        stud_list =  file1.readlines()
        print("Total students:", len(stud_list), "\n")
except :
    print("File not found")

#Task_4 - longest Name
long = ""
for i in stud_list :
    if len(long) < len(i) :
        long = i
print("longest name:", long,"\n")
    
#Given by chatgpt

longest = ""

for name in stud_list:
    name = name.strip()   # Removes \n and extra spaces
    if len(name) > len(longest):
        longest = name

print(longest)

"""Answers to the Thinking Questions
1. Why do data analysts rarely hard-code data inside programs?

Because real-world datasets:

Change frequently
Can contain thousands or millions of records
Often come from databases, CSV files, Excel files, APIs, or user uploads

If data is hard-coded, every update requires modifying the program. Reading from external files makes programs reusable and scalable.

2. What advantages do files provide over storing everything directly in code?

Files provide several benefits:

✅ Easy to update data without changing code
✅ Can store large amounts of information
✅ Easy to share between people and applications
✅ Separate data from program logic
✅ Enable automation by reading new datasets repeatedly
3. Common file formats in data analysis

You mentioned:

✅ .xlsx (Excel)
✅ .txt
✅ .csv

Those are all correct.

Some additional formats you'll encounter later:

.json
.parquet
.sql
.xml"""
