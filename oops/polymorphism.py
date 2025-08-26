#Polymorphism means “many forms”.
#In OOP, it allows the same function name to behave differently based on the object or context.

# class A:
#     def add(self,x,y):
#         print(x+y)
#     def add(self,x,y,z):
#         print(x+y+z)
    
# obj=A()
# obj.add(10,20,20)


class A:
    def add(self,*n):
        sum=0
        for i in n:
            sum=sum+i
        print(sum)
    
obj=A()
obj.add(10,20)

#method overloading (python overloading not supported),how we achieve method-over-load in  python(*args,**args),constructor over-load