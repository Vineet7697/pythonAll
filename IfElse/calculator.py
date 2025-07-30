a=int(input("enter the number:"))
b=int(input("enter the number:"))
op=(input("enter the opertor:"))

if op=="+":
   print(a+b)
elif op=="-":
    print(a-b)
elif op=="*":
    print(a*b)
elif op=="/":
    print(a/b)
elif op=="%":
    print(a%b)
elif op=="//":
    print(a//b)
elif op=="**":
    print(a**b)
else:
    print("invalid")

