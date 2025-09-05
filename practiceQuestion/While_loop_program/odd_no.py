# Write a program find odd no.(1,3,5,7,9,……) 
n=int(input("Enter the number:"))
i=1
while i<=n:
    if i%2!=0:
        print(i,end=",")
    i+=1