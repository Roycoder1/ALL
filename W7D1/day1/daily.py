# We said that NumPy is pretty much a list on steroids. Let’s see that in action.

# For the tasks below, do them using a regular Python list implementation, and then use NumPy.

# Create a table (i.e. a 2d array) of size M x N filled with random integers between 1 and 100,
# where 1 < N < 40 and 1 < M < 50.

# Print out the third row

# Print out the third column

# Set every element in the last row equal to 7

# Set every element in the last column equal the sum of the first two columns. (note: the result of
# the sum is a list which will the same length as the last column)

# import numpy as np
# import pandas as pd

# array = [[3.,4.,12.],
# [45.,27.,33.]]



# arr2D = np.random.randint(1,100,30).reshape((3,10))
# # print (arr2D)
# second = np.random.randint(1,100,40).reshape((4,10))
# # print (second)
# finalArr = arr2D,second
# print (finalArr)
# finalArr2=finalArr[0][2]
# secondcolumn= finalArr[1][2]
# print(finalArr2)
# print(secondcolumn)
# pf = pd.DataFrame(arr2D[2], index=second[2])
# print(pf)
# arr2D[0][9] = 7
# arr2D[1][9] = 7
# arr2D[2][9] = 7
# second[0][9] = 7
# second[1][9] = 7
# second[2][9] = 7
# second[3][9] = 7
# print(arr2D)
# print(second)

# arr2D[2]=arr2D[0]+arr2D[1]
# print (arr2D)
# second[3]= second[0]+second[1]+second[2]
# print (second)

import random

list = []

for i in range (10):
    rd = random.randint(1,100)
    
    list.append(rd)

print(list)


