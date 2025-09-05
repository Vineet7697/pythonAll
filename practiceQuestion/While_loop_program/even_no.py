#  Write a program to find even no. (2,4,6,8,….)

n=int(input("Enter the number:"))
i=1
while i<=n:
    if i%2==0:
        print(i,end=",")
    i+=1