

#no argument, no return type
def SI():
    p=float(input("enter principal value-"))
    r=float(input("enter rate-"))
    t=float(input("enter time period-"))
    print("simple interest=",(p*r*t)/100)
    
#SI()

#argument, return type
def SI(p,r,t):
    p=float(input("enter principal value-"))
    r=float(input("enter rate-"))
    t=float(input("enter time period-"))
    ans=(p*r*t)/100
    return ans


simple=SI(10,20,30)
print('SI',simple)