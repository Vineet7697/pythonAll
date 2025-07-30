#list, tuple, set, dictionary comprinhension
#li=[output for i in range() if]


# li=[i for i in range(1,11)]
# li=[i*i for i in range(1,11)]

# n=int(input("enter the number:"))
# li={n*i for i in range(1,11)}
# print(li)

# li=["aman","raj","rahul","pratima","gauri","prince","jatin"]
# ans=[i for i in li if len(i)>4]
# print(ans)

# li=[12,-7,5,64,-14]
# ans=[ i for i in li if i<0]
# print(ans)

# li="hello world"
# ans=[ i for i in li if  i in "aeiou"]
# print(ans)

# li=[ {i:i*i} for i in range(1,6)]
# print(li)


# data = {'item1':120,'item2':130,'item3':30}

# ans = { key:value for key,value in data.items() if value>100}
# print(ans)

# li = ["data","science","python"]

# ans = { i:len(i) for i in li}
# print(ans)
# 
# # [expression for i in <expression> if <expression> ]
# li = [ i if i%2==0 else i for i in range(1,11) if i%2==0]
# print(li)

#prime number using list comprehension
# ans = [ i for i in range(1,101) if all(i%j!=0 for j in range(2,int(i**0.5)+1)) ]
# print(ans)

# for i in range(1,101):
#     is_prime=True
#     for j in range(2,int(i**0.5)+1):
#         if i%j==0:
#             is_prime=False
#     if is_prime:
#         print(i)
        
        
# tu = ( i*i for i in range(1,11) )
# tu=list(tu)
# print(tu)
# for i in tu:
#     print(i,end=" ")

# li=[1,2,3,2]
# ans=[True if[i for i in li if li.count(i)>1] else False]
# print(ans)

# li=[i for i in range(10)]
# print(li)
# li=[i for i in range(10) if i%2==0]
# print(li)
# tu=tuple(i for i in range(10) )
# print(tu)


x=[(x,y) for x in range(2) for y in range(3)]
print(x)