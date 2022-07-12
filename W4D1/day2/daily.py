# Challenge 1
# Ask the user for a number and a length.
# Create a program that prints a list of multiples of the number until the list length reaches length.

number = int(input("Gimme a number"))
lenght = int(input("Gimme a lenght"))

for x in range(1,lenght+1):
    print(number* x )

# challenge 2 :

user = input ("Gimme a string")

string = list(dict.fromkeys(user))
string1 = ''.join(string)
print (string1)