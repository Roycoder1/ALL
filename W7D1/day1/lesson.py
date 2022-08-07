# Create a function which takes that numpy 1-D array as input and returns the following (in the same order as listed):

# * The minimum value in the array * The standard deviation of the data * The product of the elements in the array * Dot product of the array to itself * An array with 4 subtracted from every element in the input array
import numpy as np
def numpy1 ():
    input1 = input ("gimme a a list of numbers")
    input1 = int(input1)
    list = []
    list.append(input1)
    array = np.array(list)
    return array

numpy1()
# with regular python:
# import random

# for i in range (10):
#     rd=random.randint(1,100)
#     list = []
#     list.append(rd)
#     print(list)

