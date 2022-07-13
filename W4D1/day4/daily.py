# Hint: Look at the remote learning “Matrix” videos

# The matrix is a grid of strings (alphanumeric characters and spaces) with a hidden message in it.
# To decrypt the matrix, Neo reads each column from top to bottom, starting from the leftmost column, select only the alpha characters and connect them, then he replaces every group of symbols between two alpha characters by a space.

# Using his technique, try to decode this matrix:

from ast import Str


matrix = [
    '7''i''3',
    'T''s''i',
    'h''%''x',
    'i''#',
    's''M' ,
    '$''a',
    '#''t''%',
    '^''r''!',
    ]

string = str(matrix)
string1=string.replace("$", "")
string1 = string1.replace("#", "")
string1 = string1.replace("%", "")
string1 = string1.replace("!", "")
print(string1)
print(f'{string1[9]}{string1[16]}{string1[22]}{string[29]} {string[3]}{string[10]}  {string[30]}{string1[33]}{string1[44]}{string1[11]}{string1[17]}')


