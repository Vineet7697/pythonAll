#(hiding internal process)
from abc import ABC, abstractmethod #abstract class
class Senior(ABC):
    def add(self,x,y):
        print(x+y)
    def sub(self,x,y):
        print(x-y)
    @abstractmethod  #abstract method
    def div(self,x,y):
        pass
class Junior(Senior):
    def div(self):
        print("from junior class")

obj=Junior()
obj.div()

#concreate method ->abhi tak jitni bhi hamne class banayi hai vo sab concreate method hai i mean jiske andar @ method use na hua ho