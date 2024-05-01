#Array
import array as pqrs
array_elements=pqrs.array('L',[10,11,12,13,14,15])
for l in array_elements:
    print(l)

print("access first three items individually")
print(array_elements[5])

array_elements=pqrs.array('L',[10,11,12,13,14,15])
array_elements[0]=3
print(array_elements)
print(array_elements[1:4])

import array as abcd
arrayy1=abcd.array('i',[1,2,3,4,5,6])
arrayy2=abcd.array('i',[7,8,9,10])
arrayy3=arrayy1+arrayy2
print(arrayy3)

#methods and functions
import array as arr
array_ele = arr.array('i', [10,20,20,30,40,50])
array_ele2 = arr.array('i', [25,35,55])
#array_ele.append(45)
#x = array_ele.count(20)
#print(x)
#array_ele.extend(array_ele2)
#array_ele.remove(20)
#array_ele.insert(1,15)
#array_ele2.pop(1)
#array_ele.reverse()
print(len(array_ele))
print(array_ele)


