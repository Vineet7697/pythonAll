# Python program to count the total number of digits in a number. 

n=int(input("Enter the number:"))
count=0
while n!=0:
    digit=n%10
    count+=1
    n//=10
    
print(count)