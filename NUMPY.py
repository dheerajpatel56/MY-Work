import numpy as np
# my_list =[1,2,3,4]
# my_list = my_list *2
# print(my_list)
# array = np.array([[1,2,3,4]
#                   ,[5,6,7,8]])
# print(array)
# print(type(array))
# array = array*2
# print(array)
#---
# MULTI DIMENSIONAL ARRAY
#---
#array = np.array([[...n[]]])-->DIMENSIONAL and size should be same of each list
#array.shape gives you a tuple giving info abt sizes
# print(array[][][])->chain indexing
#multi dimensional indexing->array([x,y,....])
## slicing
# array[start:end:step]
# print(array[::-1])-->row
# print(array[:,::-1])--> col
# print(array[1:, 0:2])--> both row and colon
# Scalar Arithmetic --> single value
# array = np.array([1,2,3])
# applying a value to each and evry element
# print(array-1)
# print(array/4.5)
# print(array**2)

# Vectorized math functions

# radii = np.array([1,2,3])

# print(np.sqrt(array))
# print(np.round(array))
# print(np.pi)
# print(radii**2*np.pi)
#
# Element wise operations
#
# array1 = np.array([1,2,3])
# array2 = np.array([4,5,6])
# print(array1**array2)
# comparision arrays

# scores = np.array([91,55,100,73,82,64])
# print(scores < 60)
# scores[scores<60]=0 --> very good option
# print(scores)

# Broadcasting allows NumPy to perform operations on multi dimensional arrays
# with different shapes by virtually expanding dimensions
# so they match the array's shape
#The dimesnions have the same size
# OR
# One of the dimensions has a size of 1
# array1= np.array([[1,2,3,4]])
# array2=np.array([[1],[2],[3],[4]])
# # print(array1.shape)
# # print(array2.shape)
# print(array1*array2)
# array1 = np.array([[1,2,3,4,5,6,7,8,9,10]])
# array2 = np.array([[1],[2],[3],[4],[5],[6],[7],[8],[9],[10]])
# print(array1.shape)
# print(array2.shape)
# print(array1*array2)
#
# AGGREGATE FUNCTIONS-->Summarize Data and typically  return a single value
#
# array = np.array([[1,2,3,4,5],[6,7,8,9,10]])
# print(np.sum(array))
# print(np.mean(array))
# print(np.var(array)) min , max ,argmin-->index of min
# print(np.sum(array, axis=1))--> row wise sum
#
# filtering
#
# ages = np.array([[21,17,19,16,30,18,65], [39,22,15,99,18,19,20,21]])
# teenagers = ages[ages<18]
# print(teenagers)
# where function np.where(condition, arrayname,replace filtered values )-->to preserve original shape 
# GENERATE RANDOM FUNCTIONS
# rng = np.random.default_rng() 


# print(rng.integers(low=1,high=7)) high is exclusive float->uniform
# print(rng.integers(low=1, high = 101, size=(3,3)))--> set of random value s
# fruits = np.array(["apple","orange","banana","coconut","pineapple"])
# fruitsb = rng.choice(fruits, size =2)
# print(fruitsb)
# Dot product
# matrix1 = np.array([[1,2],[3,4]])
# matrix2 = np.array([[1,2],[3,4]])
# matrix3 = matrix1.dot(matrix2)
# print(matrix3)-->mat mul

 

