#super function
class hash1:
    
    def __init__(self) -> None:
        print("this is hash1 constructor")

class hash2(hash1):

    def __init__(self) -> None:
        super().__init__()
        print('this is hash2 constructor')

h2=hash2()


class star1:
    n1=int(input("enter no.-"))


class star2(star1):
    n2=int(input("enter no.-"))

    def show(self):
        print("show method of star2")
        print("n1=",self.n1)
        print(super().n1)

s2=star2()
s2.show()

class for1:
    def formethod1(self):
        print("this is formethod1 of for1 class")

class for2(for1):
    def formethod1(self):
        print("this is formethod2 of for2 class")

    def show(self):
        print("this is formethod1 of show class")

        self.formethod1()
        super().formethod1()

d2= for2()
d2.show()

