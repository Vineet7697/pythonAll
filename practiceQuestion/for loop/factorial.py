# Python program to find the factorial of a given number. 

n= int(input("Enter the number:"))

fact=1
for i in range(1,n+1):
    fact*=i
print("factorial =",fact)