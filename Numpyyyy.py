import numpy as np
#creating arrays

print (np.zeros(10, dtype='int'))

#creating a 3 row x 5 column matrix

print(np.ones((3,5), dtype=float))

#creating a matrix with a predefined value

print(np.full((3,5),1.23))

#create an array with a set sequence

print(np.arange(0, 20, 2))

#create an array of even space between the given range of values

print(np.linspace(0, 1, 5))

#create a 3x3 array with mean 0 and standard deviation 1 in a given dimension

print(np.random.normal(0, 1, (3,3)))

#create an identity matrix

print(np.eye(3))

#Array Indexing
#The important thing to remember is that indexing in python starts at zero.

x1 = np.array([4, 3, 4, 4, 8, 4])
print(x1)


#assess value to index zero
print(x1[0])

#assess fifth value
print(x1[4])

#get the last value
print(x1[-1])

#get the second last value
print(x1[-2])

#in a multidimensional array, we need to specify row and column index
x2 = np.random.randint(10, size=(3,4))
print(x2)


#1st row and 2nd column value
print(x2[2,3])

#3rd row and last value from the 3rd column
print(x2[2,-1])

#replace value at 0,0 index
print(x2)


#Array Slicing
#Now, we'll learn to access multiple or a range of elements from an array.
x = np.arange(10)
print(x)

#from start to 4th position
print(x[:5])

#from 4th position to end
print (x[4:])

#from 4th to 6th position
print(x[4:7])

#return elements at even place
print(x[ : : 2])

#return elements from first position step by two
print(x[1::2])

#reverse the array
print(x[::-1])

#You can concatenate two or more arrays at once.
x = np.array([1, 2, 3])
y = np.array([3, 2, 1])
z = [21,21,21]
print(np.concatenate([x, y,z]))

#You can also use this function to create 2-dimensional arrays.
grid = np.array([[1,2,3],[4,5,6]])
print(np.concatenate([grid,grid]))

#Using its axis parameter, you can define row-wise or column-wise matrix
print(np.concatenate([grid,grid],axis=1))

"""Until now, we used the concatenation function of arrays of equal dimension. But, what if you are required to combine a
2D array with 1D array? In such situations, np.concatenate might not be the best option to use. Instead, you can use
np.vstack or np.hstack to do the task. Let's see how!"""

x = np.array([3,4,5])
grid = np.array([[1,2,3],[17,18,19]])
print(np.vstack([x,grid]))

#Similarly, you can add an array using np.hstack
z = np.array([[9],[9]])
print(np.hstack([grid,z]))

#lso, we can split the arrays based on pre-defined positions. Let's see how!
x = np.arange(10)
print(x)


x1,x2,x3 = np.split(x,[3,6])
print(x1,x2,x3)

grid = np.arange(16).reshape((4,4))
print(grid)

upper,lower = np.vsplit(grid,[2])
print (upper, lower)

"""np.arange( ) is the best way to create large matrices with n-dimensional. By default, np.arange( ) created one
dimensional array, if you want to create 2-Dimensional or 3-Dimensional matrices, you can use np.reshape ( ) with
"""

"""np.arange(start=None, stop=None, step=None, dtype=None)
np.arange ( )
np.arange(0, 10, 3)
array([0, 3, 6, 9])

print(np.arange(0, 10, 3))"""

#Create an evenly spaced array between 1 and 60 with a difference of 2.
dif=np.arange(1,60,2)
print(dif)

#Reshape the above array into a desired shape.
print(dif.reshape(10,3))

"""Generate an evenly spaced list between the interval 1 and 8. (Take a minute here to understand the difference
between ‘linspace’ and ‘arange’)"""
gen = np.linspace(1,8,40)
print(gen)

#Now, change the shape of the array in place (‘resize’ function changes the shape of the array in place, unlike ‘reshape’)
gen.resize(10,4)
print(gen)









