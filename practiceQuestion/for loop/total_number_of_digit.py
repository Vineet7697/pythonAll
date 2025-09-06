# Python program to count the total number of digits in a number. 

n=int(input("Enter the number:"))
n=str(n)
count=0
for i in n:
    count+=1
print(count)