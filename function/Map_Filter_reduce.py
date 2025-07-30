# map method

l1=[1,2,3,4,5]
l2=[2,3,4,5]
l3=[3,4,5,6,7]

def add(x,y,z):
    return x+y+z
result=map(add,l1,l2, l3)
    
print(result)
print(list(result))


li=[1,2,3,4,5]
def square(x):
    return x**2
result=map(square,li)
print(list(result))





# filter method
li=[1,2,3,4,5,6,7,8,9,10]
def even_no(x):
    if x%2==0:
        return x
result=filter(even_no,li)
# print(list(result))
print(tuple(result))



def even_no(x):
    if x%2==0:
        return 'even'
    else:
        return 'odd'
li=[1,2,3,4,5,6,7,8,9,10]
result=map(even_no,li)
print(list(result))





# reduce method
# functools.reduce(fun_name,iterator,initial)
import functools

li=[1,2,3,4,5,6,9,8]

def max_digit(x,y):
    if x>y:
        return x
    else:
        return y
result=functools.reduce(max_digit,li,0)
print(result)
    
    
li=[1,2,3,4,5,6,9,8]

def min_digit(x,y):
    if x<y:
        return x
    else:
        return y
result=functools.reduce(min_digit,li)
print(result)



li=[1,2,3,4,5,6,9,8]

def sum(x,y):
    return x+y
    
result=functools.reduce(sum,li)
print(result)

