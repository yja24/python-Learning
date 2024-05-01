

#no argument, no return type
def SI():
    p=float(input("enter principal value-"))
    r=float(input("enter rate-"))
    t=float(input("enter time period-"))
    print("simple interest=",(p*r*t)/100)
    
#SI()
#argument, return type
def SI(p,r,t):
    ans=(p*r*t)/100
    return ans


#simple=SI(p=float(input("enter principal value-")),r=float(input("enter rate-")),t=float(input("enter time period-")))
#print('SI',simple)


def NANR():
    n1=int(input('enter desired number-'))
    n2=int(input("enter desired number-"))
    ans=n1/n2
    print(ans)

#NANR()

#argument, no return type
p1=int(input("enter number-"))
p2=int(input("enter number-"))
def product(p1,p2):
    ans=p1*p2
    print(ans)

#product(p1,p2)
# No argument, Return type
def sum():
   n1=int(input("enter number-"))
   n2 =int(input("enter number-"))
   ans = n1+n2
   return ans


#ans = sum()
#print("Sum is ", ans)


