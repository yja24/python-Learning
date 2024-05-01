#findall
import re
str="say yes to everything"
x=re.findall("yes",str)
print(x)

y=re.search("\s",str)
print(y.start())

z=re.split('\s',str)
print(z)

a=re.sub("\s","$",str)
print(a)

