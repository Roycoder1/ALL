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

# Correction:
matrix = [ 

    ["7", "i", "3"], 
    ["T", "s", "i"], 
    ["h", "%", "x"], 
    ["i", "#"," " ], 
    ["s", "M", " "], 
    ["$", "a", " "], 
    ["#", "t", "%"], 
    ["^", "r", "!"]  
]
import re
regex = "[a-zA-Z]+"
col_list = []
for row in range(0, len(matrix[0])):
    for col, char  in enumerate(matrix):
        col_list.append(matrix[col][row])

str_matrix = "".join(col_list)
clean_matrix = re.findall(regex, str_matrix)
final_matrix = " ".join(clean_matrix) 
print(final_matrix)

# Correction 2 (prof):

mat = """
    7i3
    Tsi
    h%x
    i #
    sM 
    $a 
    #t%
    ^r!
    """ 
mat_modified = mat.split('    ')
for idx, word in enumerate(mat_modified):
    mat_modified[idx] = word.strip('\n')
del mat_modified[0]
del mat_modified[-1]
mat_modified = [list(chars) for chars in mat_modified] 
col1, col2, col3 = zip(*mat_modified)
# print(col1)
# print(col2)
# print(col3)
message = ''
for l in (*col1, *col2, *col3):
    if l.isalpha():
        message += l
    elif l.isdigit():
        continue
    else:
        if message[-1] == ' ':
            continue
        message += " "
print(message)