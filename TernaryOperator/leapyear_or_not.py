n=int(input("enter the year:"))
print("leap year") if(n%4==0 and n%400==0) or n%100!=0 else print("not leap year")