#  Python program to print a multiplication table of a given number 

n=int(input("Enter the number:"))

for i in range(1,11):
    print(n,"*",i,"=",n*i)