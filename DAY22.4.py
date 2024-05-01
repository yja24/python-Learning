# 4. Create a class cal3 that will calculate simple interest. 
#Create constructor method which has three parameters .
#Create calInterest() method that will calculate Interest . 
#Create display() method that will display Interest.
p=float(input("enter principle value= "))
r=float(input("enter rate= "))
t=float(input("enter time period= "))
print("values taken")
ans=p*r*t/100

class cal3:
    def __init__(self,p,r,t) -> None:
        pass

class cal4(cal3):
    def calinterest(self):
        ans= p * r * t / 100
        pass

class cal5(cal4):

    def display(self):
        print(ans)

d=cal5()
d.display(p,r,t)