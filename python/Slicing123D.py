import numpy as np
#1D array
array1= np.arange(5)
print(array1,end="\n")
temp = array1[:]
print(temp, end="\n")
temp1 = array1[-1] #last element
print(temp1,end="\n")
temp2 =array1[::-1] #reverse
print(temp2,end="\n")

#####2D array
array1 = np.arange(12).reshape(3,4)
print(array1,end="\n")
print("Select 2nd and 3rd Row with all elements",end="\n")
temp = array1[1:3,:] # select second and third row with all elements
print(temp,end="\n")
print("Select all Row with last element",end="\n")
temp1=array1[0:3,-1]
print(temp1,end="\n")
print("Select all row with first and last element",end="\n")
temp1=array1[0:3,0:4:3] # select all row with first and last element
print(temp1,end="\n")

#####3D array
array1 = np.arange(24).reshape(2,3,4)
print(array1,end="\n")
