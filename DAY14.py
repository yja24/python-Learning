import sys
print(type(sys.argv))
print(len(sys.argv))


for i in sys.argv:
    print("values",i)

import sys 

n1=int(sys.argv[4])
n2=int(sys.argv[5])
print("sum=",n1+n2)

import sys
from math import factorial
n3= int(sys.argv[6])
ans= factorial(n3)
print("factorial is-",ans)

#while True:
   # n4= int(input("enter number- "))
   # print("number is-",n4)
    #if (n4==10):
     #   break

for i in range(1,5):
    for j in range(1,5):
        print(i," ",j)


for i in range(1,5):
    for j in range (1,4):
        print('$',end=" ")
    print()


i=1
while (i <= 5):
    j=1
    while (j<=i):
        print("* ", end=" ")
        j+=1
    i+=1
    print()
