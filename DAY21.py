import numpy as np
arr= np.array([1,3,5,7,9])
print(arr)

my_array=[]
X=int(input("size of aaray-"))

for i in range(X):
    my_array.append(int(input("enter elements-")))
my_array=np.array(my_array)

print(my_array.dtype)
print(my_array)

print(np.__version__2)