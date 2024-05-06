#Counting Characters:
#Write a Python function that takes a string as input and returns a dictionary containing the count of each character in the string.

text = input('Please enter the text')
x = {}

for i in text:
    if i in x:
        y = int(str(x[i].values())) + 1
        x[i] = y
    else:
        x[i] = 1
print(x)