# 3. Create a class cal2 that will calculate area of circle. Create setdata() methOD that that should take radius from the user, calculate area and display area.
import math
r=float(input("enter radius- "))
class cal2:
    def setdata(self,r):
        pass


class cal3(cal2):
    def display(self):
        area= math.pi*r*r
        print(area)


a=cal3()
a.display()