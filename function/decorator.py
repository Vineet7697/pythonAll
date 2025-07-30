#decorator
# from first import decor
# @decor
# def add(x,y):
#     z=x+y
#     return z
# result=add(5,5)
# print(result)



# def outer():
#     def inner():
#         print("from inner function")
#     return inner
# data=outer()
# print(data)
# x=data()



# def outer(x):
#     def inner():
#         y=x()
#         return y
#     return inner
# def x():
#     return "from function x"
# data=outer(x)
# z=data()
# print(z)


# def outer(func):
#     def inner (x,y):
#         x=x+5
#         y=y*2
#         z=func(x,y)
#         return z
#     return inner
# def add(x,y):
#     z=x+y
#     return z
# data=outer(add)
# z=data(5,10)
# print(z)


# def decor(x):
#     def inner():
#         data=x()
#         return data
#     return inner
# @decor
# def main_function():
#     return "main_function"
# x=main_function()
# print(x)



# def my_decorator(func):
#     def wrapper():
#         print("Before function runs")
#         func()
#         print("After function runs")
#     return wrapper

# @my_decorator
# def say_hello():
#     print("Hello!")

# say_hello()




# def my_decorator(func):
#     def wrapper(x, y):
#         print("Before")
#         result = func(x, y)
#         print("After")
#         return result
#     return wrapper

# @my_decorator
# def add(a, b):
#     return a + b

# print(add(3, 4))

# def my_decorator(func):
#     def wrapper(x, y):
#         print("Before")
#         result = func(x, y)
#         print("After")
#         return result
#     return wrapper
# def add(x, y):
#     z=x+y
#     return z

# data=my_decorator(add)
# z=data(5,10)
# print(z)

def decor(func):
    def inner(n):
        result=func(n)
        return result
    return inner

@decor
def add(n):
    z=even(n)
    return z
def even(n):
    even=[i*2 for i in range(1,n+1)]
    return even
print(add(10))
