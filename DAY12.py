# SINGLE LEVEL INHERITANCE 

class parent:

    def __init__(self) -> None:
        print(" parent ")

    def parentmethod(self):
        print("its parent method")


class child(parent):
       
    def childmethod(self):
        print("its child method")

myc=child()
myc.childmethod()
myc.parentmethod()


#MULTI LEVEL INHERITANCE

class Parent:
    def __init__(self) -> None:
        print("calling parent constructor")

    def parentmethod(self):
        print("its parent method")


class Child(Parent):
    def __init__(self) -> None:
        print("calling child constructor")

    def childmethod(self):
        print("calling child method")

    
class Subchild(Child):
    def __init__(self) -> None:
        print("subchild constructor")

    def subchildmethod(self):
        print("calling subchild method")

sc=Subchild()
sc.subchildmethod()
sc.parentmethod()
sc.childmethod()


# MULTIPLE INHERITANCE 
 
class Myparentclass1():

    def myparentclass1method():
        print("parentclass1 method ")

class Myparentclass2():
    
    def myparentclass2method():
        print("parentclass2 method ")

class Mychild(Myparentclass1,Myparentclass2):

    def __init__(self) -> None:
        print("child method")

mi=Mychild()
Mychild.myparentclass2method()
Mychild.myparentclass1method()


# HIERARCHICAL INHERITANCE

class PARENT:
    def __init__(self) -> None:
        print("main parent data")

    def PARENTmethod():
        print("main parent data")

class CHILD1(PARENT):
    def CHILD1method():
        print("child1 data")

class CHILD2(PARENT):
    def CHILD2method():
        print("child2 data")

hi=CHILD2()
hii=CHILD1()
CHILD2.CHILD2method()
CHILD1.CHILD1method()

# HYBRID INHERITANCE

class HYparent1():
    
    def HYparentmethod1():
        print(" HY parent method")


class HYparent2():
    def HYparentmethod2():
        print("HY parent method2")


class HYchild1(HYparent1,HYparent2):

    def HYchildmethod1():
        print("child1 meth")

class HYchidl2(HYparent2): 

    def HYchild2method():
        print("child 2 method")


hy=HYchidl2()
HYchidl2.HYchild2method()
HYchidl2.HYparentmethod2()



