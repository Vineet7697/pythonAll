# Python program that accepts a word from the user and reverses it. 

str=input("enter the string:")
reverse=""
for i in str:
    reverse=i+reverse
print("revrse string=",reverse)