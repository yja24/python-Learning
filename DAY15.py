# lambda function 
value = lambda : "why not"
print(value())

#
ans= lambda a:a+5
print("answer is",ans(int(input("enter a- "))))

#
ans= lambda a,b:a/b
a=int(input("enter value of a-"))
b=int(input("enter value of b-"))
print(ans(a,b))

#normal vs lambda
n1=int(input("enter value of n1-"))
def squares(n1):
    return n1*n1
print(squares(n1))


ans=lambda n1:n1*n1
print(ans(int(input("enter value of n1-"))))


#filter()
mylist=[10,20,30,40,50]
ans= list(filter(lambda a:a%4==0,mylist))
print(ans)


#map()
mylist2=[100,200,300,400,500,600,700]
ans=list(map(lambda a:a/2,mylist2))
print(ans)


#reduce
from functools import reduce
mylist3= ['l','a','p','t','o','p']
ans= reduce((lambda a,b:a+b),mylist3)
print(ans)