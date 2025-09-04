# Write a program to find given year is leep year or not.

year=int(input("Enter the number:"))

if ((year%4==0 and year%400==0) or year%100!=0):
    print("leap year")

else:
    print("not leap year")