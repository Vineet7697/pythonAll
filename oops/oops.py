# class Student:
#     def __init__(self,name):
#         self.name=name
        
# # obj1=Student
# # print(id(Student))
# # print(id(obj1))
#     def stu_detail(self):
#         print(self.name)
#         print(self.age)

# obj1=Student('vineet')
# print(id(obj1))
# print(id(Student))
# print(id(obj1.name))

# obj1.age=10
# obj1.stu_detail()

# instance variable
class Student:
    def __init__(self,name,age,roll):
        self.n=name
        self.a=age
        self.r=roll
    def show(self):
        print(self.n)
        print(self.a)
        print(self.r)
obj1=Student('vineet',23,110)
obj2=Student('rohit',21,120)

obj1.show()
obj2.show()