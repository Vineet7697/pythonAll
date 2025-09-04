# write a program to find largest no among the three inputs numbers.

a=int(input("Enter any number1:"))
b=int(input("Enter any number2:"))
c=int(input("Enter any number3:"))
if a==b and b==c:
    print("invalid number")
elif a>b and a>c:
    print("a is the largest number")

elif b>a and b>c:
    print("b is the largest number")
    
else:
    print("c is the largest number")