
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

###hierarchical inheritence
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

### hybrid inheritence
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