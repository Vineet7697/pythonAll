# Write a program to find squre root of given no. 

num=int(input("Enter the number:"))

if num<0:
    print("Square root of negative number is not real.")
else:
    sqrt=num**0.5
    print("sqare roo of",num,"is",sqrt)