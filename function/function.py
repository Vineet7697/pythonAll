#non return without arguments

# def multi():
#     a=int(input("enter the number:"))
#     b=int(input("enter the number:"))
#     print(a*b)
# multi()


#non return with arguments

# def multi(a,b):
#     print(a*b)
# x=int(input("enter the number:"))
# y=int(input("enter the number:"))
  
# multi(x,y)



# return type without argument

# def multi():
#     a=int(input("Enter a Number: "))
#     b=int(input("Enter a Number: "))
#     return a*b

# ans=multi()
# print(ans)



# #return type with argument

# def multi(b,a):
#     return a*b
# #user input
# a=int(input("Enter a Number: "))
# b=int(input("Enter a Number: "))
# ans=multi(a,b)
# print(ans)


# # print 1 to 10
# def printonetoten():
#     for i in range(11):
#         yield i
# ans=printonetoten()
# print(ans)
# for i in ans:
#     print(i,end=" ")



#  # prime number
# def is_prime(num):
#     for i in range(2,num):
#         if num%i==0:
#             return "Not a Prime"
#     return "Prime"
# print(is_prime(8))



# # factorial
# def factorial(n):
#     fact=1
#     for i in range(1,n+1):
#         fact=fact*i
#     return fact
# ans=factorial(5)
# print(ans)



# #fibonacci series
# def fibo(n):
#     a=0
#     b=1
#     for i in range(n):
#         print(a,end=" ")
#         c=a+b
#         a=b
#         b=c
# ans=fibo(8)
# print(ans)



# # even
# def even(n):
#     for i in range(n+1):
#         if i%2==0:
#             print(i)
# num=int(input("Enter the number:"))
# even(num)



# # odd
# def odd(n):
#     for i in range(n+1):
#         if i%2!=0:
#             print(i)
# num=int(input("Enter the number:"))
# odd(num)



# # sum of n number
# def sum(n):
#     sum=0
#     for i in range(n+1):
#         sum+=i
#     return sum
# num=int(input("Enter the number:"))
# ans=(sum(num))
# print("Sum=",ans)



# # square of list
# def square(n):
#     for i in n:
#         print(i*i)
# li=[1,2,3,4,5]
# square(li)



# # palimdrome number
# def palindrome(n):
#     reverse=0
#     while n>0 :
#         digit=n%10
#         reverse=reverse*10+digit
#         n//=10
#     return reverse
# num=int(input("enter the number:"))
# ans=palindrome(num)
# if ans==num:
#     print("palindrome")
# else:
#     print("not palindrome")
    
    
    
# # reverse number
# def reverse(n):
#     reverse=0
#     while n>0:
#         digit=n%10
#         reverse=reverse*10+digit
#         n//=10
#     return reverse
# num=int(input("enter the number:"))
# ans=reverse(num)
# print(ans)




# # sum of digit
# def sum_of_digit(n):
#     sum=0
#     while n>0:
#         digit=n%10
#         sum=sum+digit
#         n//=10
#     return sum
# num=int(input("enter the number:"))
# ans=sum_of_digit(num)
# print(ans)



# # write a program to find the HCF of two number
# def hcf(n1,n2):
#     hcf=1
#     for i in range(n1,n2):
#         if n1%i==0 and n2%i==0:
#             hcf=i
#     return hcf
# num1=int(input("Enter the number:"))
# num2=int(input("Enter the number:"))
# ans=hcf(num1,num2)
# print(ans)



# # write a program to find the LCM of two number
# def lcm(n1,n2):
#     lcm=1
#     for i in range(1,n2):
#         if n1%i==0 and n2%i==0:
#             lcm=i
#     lcm=(num1*num2)//lcm
#     return lcm
# num1=int(input("Enter the number:"))
# num2=int(input("Enter the number:"))
# ans=lcm(num1,num2)
# print(ans)



# # write a program to find the sum of even and odd number seperately in a range
# def sum_even_odd(n1,n2):
#     sum_even=0
#     sum_odd=0
#     for i in range(num1,num2+1):
#         if i%2==0:
#             sum_even+=i
#         else:
#             sum_odd+=i
#     print("sum_even",sum_even)
#     print("sum_odd",sum_odd)
# num1=int(input("enter the number:"))
# num2=int(input("enter the number:"))
# sum_even_odd(num1,num2)



#  # write a program to calculate the sum of squares of the first N natural numbers
# def sum_of_square(n):
#     sum=0
#     for i in range(1,n+1):
#         sum+=i*i
#     return sum
# num=int(input("enter the number:"))
# ans=sum_of_square(num)
# print(ans)



# # print the multiplication  table of a number
# def multiplication_table(n):
#     for i in range(1,11):
#         print( n*i)
# num=int(input("enter the numebr:"))
# multiplication_table(num)




# # implement the program to count the number of digits in a number
# def count_number_digit(n):
#     count=0
#     while n!=0:
#         count+=1
#         n//=10
#     return count
# num=int(input("Enter the number:"))
# ans=count_number_digit(num)
# print("Digit=",ans)



# #remove the duplicate element
# def remove_duplicate(li):
#     list=[]
#     for i in li:
#         ans=False
#         for j in list:
#             if i==j:
#                 ans=True
#         if not ans:
#             list.append(i)
#     return list

# li=[1,1,2,2,3,4,5,6,4]
# print(remove_duplicate(li))


# # leap year
# def year(n):
#    if n%4==0 and n%400==0 and n%100==0:
#        print("leap year")
#    else:
#        print("not leap year")
# num=int(input("enter the year:"))
# year(num)


# # vowel or consonant in string
# def vowel_consonant(str):
#     vowel=0
#     consonant=0
#     for i in str:
#         if i in "aeiou":
#             vowel+=1
#         elif i in "qwrtypsdfghjklmnbvcxz":
#             consonant+=1
#     print("vowel=",vowel)
#     print("consnant=",consonant)
# s="hello python121!"
# vowel_consonant(s)



# # count frequency of character
# def frequency(str):
#     ans={}
#     for i in str:
#         # if i in ans:
#         #     ans[i]=ans.get(i)+1
#         # else:
#         #     ans[i]=1
#         ans[i]=ans.get(i,0)+1
#     return ans
# s="hello"
# print(frequency(s))


# # Anagram
# def Anagram(str1,str2):
#     if len(str1)!=len(str2):
#         print("not anagram")
#     else:
#         ans={}
#         for i in str1:
#             ans[i]=ans.get(i,0)+1
#         for j in str2:
#             if j in ans:
#                 ans[j]-=1
#         freq=True
#         for i in ans.values():
#             if i!=0:
#                 freq=False
#         if freq:
#             print("anagram")
#         else:
#             print(not Anagram)
# s1="silent"
# s2="listen"
# Anagram(s1,s2)


# # non repeative string
# def Non_repeat(str):
#     for i in range(len(str)):
#         count=0
#         for j in range(len(s)):
#             if  s[i]==s[j]:
#                 count+=1
#         if count==1:     
#             print(s[i],end=" ")
# s="programing"
# Non_repeat(s)



# GCD
# def is_gcd(num1,num2):
#     while num2!=0:
#         temp=num2
#         num2=num1%num2
#         num1=temp
#     return(num1)
# a=int(input("Enter the first number:"))
# b=int(input("Enter the second number:"))
# print(is_gcd(a,b))



# def add(x,y):
#     z=x+y
#     print(z)
# add(4,5)




# def add(x,y):
#     z=x+y
#     return z
# print(add(4,5))




# keyword arguments
# def new(x,y,z):
#     print(x,y,z)
#     return x+y+z
# print(new(z=5,y=4,x=3))


# variable length keyword arguments
# def mydict(** kwargs):
#     print(kwargs)
#     print(type(kwargs))
# mydict(x=10,y=20,z=30,p=40,q=50)

# mydict={'x': 10, 'y': 20, 'z': 30, 'p': 40, 'q': 50}
# sum=0
# for i in mydict.values():
#     sum+=i
# print(sum)


# def mydict(** kwargs):
#     sum=0
#     for i in kwargs.values():
#         sum+=i
#     return sum
# print(mydict(x=10,y=20,z=30,p=40,q=50))



#


# def is_prime(x):
#     flag=True
#     for i in range(2,x):
#         if x%i==0:
#             flag=False
#             break
#     if flag==True:
#         print("prime number")
#     else:
#         print("not prime number")
        
# n=int(input("enter the number:"))
# is_prime(n)


# def year(n):
#     if (n%4==0 and n%100!=0) or n%400==0:
#         print("leap year")
#     else:
#         print("not leap year")
    
# num=int(input("enter the number:"))
# year(num)







# import datetime

# now = datetime.datetime.now()
# print("Current date and time:", now)

# print("Year:", now.year)
# print("Month:", now.month)
# print("Day:", now.day)
# print("Hour:", now.hour)
# print("Minute:", now.minute)
# print("Second:", now.second)


# from datetime import datetime, timedelta

# now = datetime.now()
# print("Now:", now)

# # Add 7 days
# future = now + timedelta(days=7)
# print("7 days later:", future)

# # Subtract 2 hours
# past = now - timedelta(hours=2)
# print("2 hours ago:", past)


# delta = timedelta(days=1, hours=5, minutes=30)
# print(delta)  
