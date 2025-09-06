#  Python program to get the Fibonacci series. (0,1,1,2,3,5,8,13,21……………..) 
n=int(input("Enter the number:"))

a=0
b=1
print(a,b,end=" ")
for i in range(2,n):
    c=a+b
    print(c,end=" ")
    a=b
    b=c