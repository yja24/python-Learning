#EXCEPTIONS
try:
    n1=int(input("enter no.1- "))   
    n2=int(input("enter no.2- "))
    ans=n1/n2
    print("ans",ans)
except ZeroDivisionError:
    print("number cannot be divided by zero")

try:
    n1=int(input("enter no.1- "))   
    n2=int(input("enter no.2- "))
    ans=n1/n2
    print("ans",ans)
except Exception:
    print("number cannot be divided by zero")

try:
    n1=int(input("enter no.1- "))   
    n2=int(input("enter no.2- "))
    ans=n1/n2
    print("ans",ans)
except:
   print("number cannot be divided by zero")

try:
    n1=int(input("enter no.1- "))   
    n2=int(input("enter no.2- "))
    ans=n1/n2
    print("ans",ans)
except ZeroDivisionError:
    print("number cannot be divided by zero")
except ValueError:
    print("numbers only")
else:
    print("thanku")
finally:
    print("NEXT")

