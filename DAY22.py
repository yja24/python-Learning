#major tasks
# 1. create a class demo. this is class should have one parameterized method called showAns(). 
#this method will check if a number is +ve, 0 or -ve.

n1=int(input("enter yout desired number- "))

    
class demo:
        
    def showAns(self,n1):
        if n1==0:
                print("Zero")
        elif n1<0:
                print("-ve")
        else:
                print("+ve")

calling=demo()
calling.showAns(n1)