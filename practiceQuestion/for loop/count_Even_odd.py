n=int(input("enter the number:"))
even_count=0
odd_count=0

for i in range(n+1):
    if i%2==0:
        even_count+=1
    else:
        odd_count+=1
print("Even_count=",even_count)
print("odd_count=",odd_count)