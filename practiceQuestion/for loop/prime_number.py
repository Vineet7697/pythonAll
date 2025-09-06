# Python program to display all numbers within a range except the prime numbers. 

n1=int(input("Enter the number:"))

for num in range(1,n1+1):
    is_prime=True
    for i in range(2,num):
        if num%i==0:
            is_prime=False
            break
    if is_prime:
        print(num,end=" ")