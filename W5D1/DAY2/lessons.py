# # class Circle:
# #     color = "red"

# # class NewCircle(Circle):
# #     color = "blue"

# # nc = NewCircle
# # print(nc.color)
# # # >> What will be the output ?
# # # The output will be blue because the child class overwrite parents class

# # class Circle:
# #     def __init__(self, diameter):
# #       self.diameter = diameter

# #     def grow(self, factor=2):
# #         """grows the circle's diameter by factor"""
# #         self.diameter = self.diameter * factor

# # class NewCircle(Circle):
# #     def grow(self, factor=2):
# #         """grows the area by factor..."""
# #         self.diameter = (self.diameter * factor * 2)

# # nc = NewCircle(1)
# # print(nc.diameter)

# # nc.grow()

# # print(nc.diameter)
# # >> What will be the output
# # OUTPUT 4

# # Try to recreate the class explained below:

# # We have a class called Door that has an attribute of is_opened declared when an instance is initiated.

# # We can create a class called BlockedDoor that inherits from the base class Door.

# # We just override the parent class's functions of open_door() and close_door() with our own BlockedDoor version of those functions, which simply raises an Error that a blocked door cannot be opened or closed.

# class Door ():
#     def __init__(self,is_opened) -> None:
#         self.is_opened = is_opened
#     def open(self):
#         self.is_opened = True
#         print("Door is open")
#     def close (self):
#         self.is_opened = False
#         print("Door is closed")

# class BlockedDoor(Door):
#     def __init__(self) -> None:
#         self.is_opened = False

#         # self.close_door = close_door
#         # is_opened = print("Error a block door can't be open")
#     def open(self):
#        raise Exception("Cannot open blocked door")
#         # print("Door is open")
#     def close (self):
#         raise Exception("Cannot open blocked door")


# door = Door()
# door.open()
# door.close()
# print(door.is_opened)
# BlockedDoor = BlockedDoor()
# # blocked_door.close()




# block = BlockedDoor(1,0)
# print(block.is_opened)
# print(block.close_door)

my_list = [2,3,1,2,"four",42,1,5,3,"imanumber"]

sum = 0
number_count =0
for item in my_list:
    try:
        sum+=item
    except:
        continue
    else:
       continue
    finally:
        pass

else:
    print(sum)

# 🌟 Exercise 2 : Dogs
# Instructions
# Create a class called Dog with the following attributes name, age, weight.
# Implement the following methods in the Dog class:
# bark: returns a string which states: “<dog_name> is barking”.
# run_speed: returns the dogs running speed (weight/age*10).
# fight : takes a parameter which value is another Dog instance, called other_dog. This method returns a string stating which dog won the fight. The winner should be the dog with the higher run_speed x weight.

# Create 3 dogs and run them through your class.

class Dog 