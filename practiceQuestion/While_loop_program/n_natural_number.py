
#  Write a program to display n natural numbers. (In Horizontal 1,2,3,4,5…….. ) 


n=int(input("Enter the number:"))
i=1
while i<=n:
    if i!=n:
        print(i,end=",")
    else:
        print(i)
    i+=1