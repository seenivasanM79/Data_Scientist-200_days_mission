#DAY - 6

#TASK - 1 String Basics
text  = "Data Science is the future"

#length of the string
print("Length of the string :", len(text))


#Convertting string to upper and lower case
print("UPPERCASE :", text.upper())
print("lowercase:", text.lower())

#count number of words
def count(str):
    if len(str) > 0:
        counting = 1
        for i in str:
            if i == " ":
                counting+= 1
    else :
        counting = 0
    return counting

print("Number of words :",count(text))

#Replace "future" -> "present"
print("Replacing the word the future with present:",end=" ")
print(text.replace("future","present"))

#Task - 2 Function: vowel counter
def count_vowels(text):
    l_text = text.lower()
    vowels = ["a", "e", "i", "o", "u"]
    count = 0
    for j in l_text :
        if j  in vowels:
            count +=1
    return count
print("Count of Vowels in the text:",count_vowels(text))

#Text Cleaning

raw_text = "  AI!!! is $$$ powerful ###  "
cleaned_text = ""

for ch in raw_text:
    if ("A" <= ch <= "Z") or ("a" <= ch <= "z") or ("0"<= ch <= "9") or (ch == " "):
        cleaned_text += ch

cleaned_text = cleaned_text.lower()
cleaned_text = " ".join(cleaned_text.split())

print(cleaned_text)
