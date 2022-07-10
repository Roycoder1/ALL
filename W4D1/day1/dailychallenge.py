# Using the input function, ask the user for a string. The string must be 10 characters long.
# If it’s less than 10 characters, print a message which states “string not long enough”.
# If it’s more than 10 characters, print a message which states “string too long”.

from xml.dom.pulldom import CHARACTERS


stringUser = input('Choose for a string')

if len(stringUser) <10 :
    print('string not long enough')

else:
    print('string too long')

# Then, print the first and last characters of the given text.

print (stringUser[0][0])
last_char = stringUser[-1]
print(last_char)

# Using a for loop, construct the string character by character: Print the first character, then the second, then the third, until the full string is printed. For example:

for character in  'Hello World':
    print(character)

   