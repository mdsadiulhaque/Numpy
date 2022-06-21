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

print(x1 = np.array([4, 3, 4, 4, 8, 4]))
print(x1)

#assess value to index zero
print(x1[0])

#assess fifth value
print(x1[4])

#get the last value
pint(x1[-1])

#get the second last value
print(x1[-2])

#in a multidimensional array, we need to specify row and column index
print(x2 = np.random.randint(10, size=(3,4)))
print(x2)

