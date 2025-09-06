# Python program that accepts a string and calculates the number of digits and letters. 

str=input("enter the str and digit:")

digit=0
letter=0

for i in str:
    if i.isdigit():
        digit+=1
    elif i.isalpha():
        letter+=1
print("Digit=",digit)
print("Letter",letter)
