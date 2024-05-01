#abstraction 
from abc import ABC, abstractmethod

class structure(ABC):
    def structure1(self):
        print("this is structure1")

    @abstractmethod
    def area(self):
        pass

class Square(structure):
    def __init__(self,side) -> None:
        self.side= side
    def area(self):
        ans=self.side*self.side
        print("area of the square is-",ans)
        
class Rectangle(structure):
    def __init__(self,l,b) -> None:
        self.l=l
        self.b=b

    def area(self):
        ans=self.l*self.b
        print("area of rectange is-",ans)

s1=Square(int(input("enter dimension of side-")))
s1.structure1()
s1.area()

r1=Rectangle(int(input("enter length-")),int(input("enter breath-")))
r1.structure1()
r1.area()