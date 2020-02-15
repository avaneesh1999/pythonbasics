from numpy import *


arr1 = array([1,3,4,5,6])
arr2 = array([7,8,9,10,12])

print(concatenate([arr1,arr2])) # functions like sin,cos,log,sqrt can also be used.

arr3 = array([10,20,30,40])
arr4=arr3
arr4.view()#is used change the id of the array
print(arr3)
print(arr4)
print(id(arr3))
print(id(arr4))