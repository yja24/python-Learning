n1=13
n2=12
n3=10
#number to string
n1=str(n1)
n2=str(n2)
n3=str(n3)

print(n1,type(n1))
print(n2,type(n2))
print(n3,type(n3))


#list to tuple
mylist=[12,23,34,'yes','no','what']

tuple1=tuple(mylist)
print(tuple1)
print(type(tuple1))

#tuple to list
mytuple=(12,23,34,'yes','no','what')

list1=list(mytuple)
print(list1)
print(type(list1))


#dictionary to tuple n list
mydict={1:'true',2:'false',3:'depends'}
mylistx=list(mydict.values())
print(mylistx)
print(type(mylistx))
mytupley=tuple(mydict.values())
print(mytupley)
print(type(mytupley))