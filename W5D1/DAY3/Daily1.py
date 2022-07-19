# Instructions :
# The goal is to create a class that represents a simple circle.
# A Circle can be defined by either specifying the radius or the diameter.
# The user can query the circle for either its radius or diameter.

# Other abilities of a Circle instance:

# Compute the circle’s area
# Print the circle and get something nice
# Be able to add two circles together
# Be able to compare two circles to see which is bigger
# Be able to compare two circles and see if there are equal
# Be able to put them in a list and sort them
import turtle

class Circle():

    def __init__(self,diameter) -> None:
        self.diameter = diameter
    
    def add (self):
        sum = userCircle1+userCircle2
        print (sum)
        if userCircle1>userCircle2:
            print ('Circle 1 is higher')
        if userCircle1 == userCircle2:
            print("Two circles are equal")
        else:
            print ("Circle 2 is higher")
    def list(self):
        
        list = [userCircle1]
        list.append(userCircle2)
        print (list)
        sorted(list)
        print(sorted(list))


    

userCircle1 = input("Draw the circle with a number ")
userCircle2 = input("Draw the second circle with a number ") 
userCircle1 = int(userCircle1)
userCircle2 = int(userCircle2)
turtle.circle(userCircle1)
turtle.circle(userCircle2)
Circle.add(userCircle1+userCircle2)
Circle.list(userCircle1+userCircle2)

