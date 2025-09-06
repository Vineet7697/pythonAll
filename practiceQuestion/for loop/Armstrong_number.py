# Python program to check if a given number is an Armstrong number. (153=1**3+5**3+3**3) 

num=int(input("Enter the number:"))
n=len(str(num))
sum=0
for i in str(num):
    sum+=int(i)**n
if(sum==num):
    print("armstrong number")
else:
    print("not armstrong number")