import numpy as np
# a = np.array([[1,2,3],[4,5,6],[7,8,9]])
# print(a.reshape([-1]))
# arr1 = np.ones((3,3,2))
# arr2 = np.ones((3,3))
# print(arr1)
# print(arr2)

a=np.zeros((2,2,2))
a[:,:,0]=([[3,6],[5,8]])
a[:,:,1]=([[2,5],[7,2]])
b=np.zeros((2,2,2))
b[:,:,0]=([[3,2],[9,6]])
b[:,:,1]=([[7,8],[1,0]])
c=np.dot(a,b)
print(c)