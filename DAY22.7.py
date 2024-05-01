#7.Consider an employee class, which contains fields such as name and designation. And a subclass, which contains a field salary. Write a program for inheriting this relation. Create necessary methods or constructors to display all values.

name=input("enter your name-- ")
designation=input("enter your designation-- ")



class employee:
    def employeedeatils(self,name,designation) -> None:
        name==name
        designation==designation
        pass

class salary(employee):
    def salarydeatils(self,name,designation):
        name==name
        if designation=="manager":
            print(" 1 cr")
        elif designation=="ceo":
            print("2cr") 
        else:
            print("80k")    

d1=employee()
d1.employeedeatils(name,designation)

d2=salary()
d2.salarydeatils(name,designation)
