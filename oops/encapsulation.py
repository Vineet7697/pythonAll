
# 1.public variable/method
# class A:
#     principle='python'
#     def show(self):
#         print(A.principle)
# class B(A):
#     def new(self):
#         print(A.principle)

# obj=B()
# obj.new()
# obj.show()
# print(A.principle)


# 2.protected variable/method(not supported in python)
# class A:
#     _principle='python'
#     def _show(self):
#         print(A._principle)
# class B(A):
#     def new(self):
#         print(A._principle)

# obj=B()
# obj.new()
# obj._show()
# print(A._principle)

# 3.private variable/method(not supported in python)
class A:
    __principle='python'
    def __show(self):
        print(A.__principle)
class B(A):
    def new(self):
        print(A.__principle)

obj=B()
# obj.new()  #error
# obj.__show()  #error
# print(A.__principle)  #error

# A.__show()  #error
print(dir(A))
print(A._A__principle)