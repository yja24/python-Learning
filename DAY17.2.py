import re
mystr="Harman and Kardon "
a=re.findall("[a-l]",mystr)
print(a)

txt="date of birth is 14/11/2004"

b=re.findall("\d",txt)
print(b)

c=re.findall("Har...",mystr)
print(c)

d=re.findall("^Harman",mystr)
if d:
    print("it starts with",d)
else:
    print("no match")

e=re.findall("Kardon$",mystr)
print("Kardon")

f=re.findall("ax*",mystr)
print(f)

g=re.findall("Harman|Willsons",mystr)
print(g)
if g:
    print("yes")
else:
    print("no")

