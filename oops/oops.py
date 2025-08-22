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
# class Student:
#     school='shss'
#     def __init__(self,name,city):
#         self.name=name
#         self.city=city
        
#     @classmethod
#     def update(cls,new):
#         print(id(cls))
#         cls.school=new
#     def show(self):
#         print(self.name, self.city, Student.school)

# print(id(Student))
# obj1=Student('vineet','bhopal')
# obj2=Student('neeraj','bhopal')
# Student.update('new_shss')
# obj1.show()
# obj2.show()


######inheritence

# class Parent:
#     def home(self):
#         print("parent home")
# class child(Parent):
#     pass
# obj=child()
# obj.home()

#method overriding
# class Parent:
#     #method
#     def home(self):
#         print("parent home")
# class Child(Parent):
#     #method
#     def home(self):
#         print("child home")
#         super().home() #super keyword parent class ke method ko print karta hai
# obj=Child()
# obj.home()


#### multilevel inhritence

# class GrandParent:
#     def bank(self):
#         print("hdfc")
#     def home(self):
#         print("grandparent home")
# class Parent(GrandParent):
#     pass
# class Child(Parent):
#     pass
# obj=Child()
# obj.bank()
# obj.home()


### multiple inheritence
# class A:
#     def home(self):
#         print("home from A class")
# class B:
#     def bank(self):
#         print("bank from B class")
#     def home(self):
#         print("home from B class")
# class C(A,B):
#     pass
# obj=C()
# obj.bank()
# obj.home()

#hierarchical inheritence
# class A:
#     def home(self):
#         print("home from A class")
# class B(A):
#     def home(self):
#         print("home from B class")
# class C(A):
#     def home(self):
#         print("home from C class") 
# obj1=C()
# obj1.home()
# obj2=B()
# obj2.home()

# hybrid inheritence
class A:
    def home(self):
        print("home from A class")
        
class B:
    def bank(self):
        print("bank from B class")
class C(A,B):
    def bank(self):
        print("bank from C class")
class D(C):
    def bank(self):
        print("bank from D class")
class E(C):
    pass
obj1=E()
obj1.home()
obj1.bank()
obj2=D()
obj2.home()
obj2.bank()
# inheritence, type of inheritence, method overriding , Super(), MRO(method resolution order)