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
# class Student:
#     def __init__(self,name,age,roll):
#         self.n=name
#         self.a=age
#         self.r=roll
#     def show(self):
#         print(self.n)
#         print(self.a)
#         print(self.r)
# obj1=Student('vineet',23,110)
# obj2=Student('rohit',21,120)

# obj1.show()
# obj2.show()

#static method
# class Student:
#     def __init__(self,name,city):
#         self.name=name
#         self.city=city
#     @staticmethod
#     def add():
#         print(self.name)
#         print(self.city)
# obj1=Student('vineet','bhopal')

# obj1.add()



#class method
class Student:
    school='shss'
    def __init__(self,name,city):
        self.name=name
        self.city=city
        
    @classmethod
    def update(cls,new):
        print(id(cls))
        cls.school=new
    def show(self):
        print(self.name, self.city, Student.school)

print(id(Student))
obj1=Student('vineet','bhopal')
obj2=Student('neeraj','bhopal')
Student.update('new_shss')
obj1.show()
obj2.show()
