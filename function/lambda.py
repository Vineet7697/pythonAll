
# x=lambda x,y:print(x+y)
# x(4,5)

# x=lambda x,y:x+y
# print(x(4,5))

# x=lambda x,y:print(x+y)
# print(x(4,5))



li=[1,2,3,4,5,6,7,8,9]
result=filter(lambda x: x if x%2==0 else None,li)
print(list(result))


# li=[1,2,3,4,5,6,7,8,9]
# result=map(lambda x: 'even' if x%2==0 else 'odd',li)
# print(list(result))




from functools import reduce
# # sum of number
# li=[1,2,3,4,5,6,7,8,9]
# result=reduce(lambda x,y:x+y,li)
# print(result)

# greater value
li=[1,2,3,4,5,6,7,8,9]
result=reduce(lambda x,y: x if x>y else y,li)
print(result)

# li=[1,2,3,4,5,6,7,8,9]
# x=[lambda x,i=i:i for i in li] 
# for f in x:
#     print(f(0))
