#dimensions
import numpy 
arr=numpy.array(int(input("enter value-")))
print(arr)


arrr=numpy.array([14, 11, 20])
print(arrr) 
print(type(arrr))


arrrr=numpy.array([[2,3,4],['a','b','c']])
print(2,2)

arrrrr= numpy.array([[[2,3,4],[5,6,7]],[[8,9,0],[0,1,2]]])
print(arrrrr)

print(arr.ndim)
print(arrr.ndim)
print(arrrr.ndim)
print(arrrrr.ndim)

print(arrr[2])
print(arrrr[1,2])
print(arrrrr[0,0,0])