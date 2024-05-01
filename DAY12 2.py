#Create a class called Demo.This is class should have one parameterized method called showAns(). This method will check if a number is zero,positive or negative.


n1=int(input("Enter Number- "))


class DEMO:

    def showans(self,n1):
        
        if n1 < 0:
            print("number is negative")

        elif n1 == 0:
            print("n1 is equal to 0")

        else:
            print("n1 is positive")

d=DEMO()
d.showans(n1)
        
        
# create a class cal1 that will calculate sum of three numbers. create setdata()method which has three parameter that contain numbers. create display()method that will calculate sum and display sum.

n1=float(input("Enter first number-"))
n2=float(input("Enter second number-"))
n3=float(input("Enter third number-"))
class cal1:
    def setdata(n1,n2,n3):
        n1==n1,n2==n2,n3==n3
        ans=n1+n2+n3
        print("answer = ",ans)

d2=cal1()
cal1.setdata(n1,n2,n3)

