#numpy array slicing
import numpy

arr= numpy.array(['y','u','v','r','a','j'])
print(arr[0:6])
print(arr[:])
print(arr[:3])
print(arr[::2])

arrr=numpy.array([[2,3,4,5],[4,5,6,7]])
print(arrr[0,0:2])

print(arr.dtype)

ar=numpy.array(['y','u','v','r','a','j'],dtype='S')
print(ar.dtype)

ar1=numpy.array([10.3,33.4,44.5])
newarr=ar1.astype('i')
print(newarr)
print(newarr.dtype)

ar2=numpy.array([12.3,0.0,0.0,7.8])
newarr=ar2.astype(bool)
print(newarr)
print(newarr.dtype)