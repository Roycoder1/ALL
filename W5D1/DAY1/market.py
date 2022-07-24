# class Farm (): #the farm class should be implemented with class and the name Farm 
    
#     def __init__(self,farmName,name,age) -> None:#__init__ method is necessary for defining the name of the farm 
#         self.farmName = farmName
#         self.name=name
#         self.age= age
#         print(f"{self.farmName}'s farm")
#         self.animals1 = {}
        
#     def add_animal(self):#Needs only add_animal method and get_info method
     
#         self.list = []
#         print(f"{self.name}: {self.age}")
        
    
#     def get_info(self):
#         print("E-I-E-I-0")
#     def get_animal_types(self):
       
#         listFarms = [self.name]
#         listFarms = sorted(listFarms)
#         return listFarms
        
#     def get_short_info(self):
#         # name1 = "cow"
#         # name2 = "sheep"
#         # name3 = "goat"
#         listFarms = [self.name]
#         listFarms = sorted(listFarms)
        

#         print(f"McDonald’s farm has{self.name} {self.name} and {self.name} ")



# macdonald = Farm("McDonald",'cow',5)
# macdonald1 =Farm("McDonald",'sheep',2)
# #It should have 2 elements otherwise it will be an error
# macdonald2 = Farm("McDonald",'goat', 12)
# macdonald.get_info()
# macdonald.get_animal_types()
# macdonald.get_short_info()

# eXPAND THE Farm

# Instructions : Old MacDonald’s Farm
# Take a look at the following code and output:
# File: market.py

# macdonald = Farm("McDonald")
# macdonald.add_animal('cow',5)
# macdonald.add_animal('sheep')
# macdonald.add_animal('sheep')
# macdonald.add_animal('goat', 12)
# print(macdonald.get_info())
# Output

# McDonald's farm

# cow : 5
# sheep : 2
# goat : 12

#     E-I-E-I-0!


# Create the code that is needed to receive the result provided above. Below are a few questions to assist you with your code:

# 1 - Create a class called Farm. How should it be implemented?
# 2 - Does the Farm class need an __init__ method? If so, what parameters should it take?
# 3 - How many methods does the Farm class need?
# 4 - Do you notice anything interesting about the way we are calling the add_animal method? What parameters should this function have? How many…?
# 5 - Test your code and make sure you get the same results as the example above.
#   Bonus: nicely line the text in columns as seen in the example above. Use string formatting.

# Expand The Farm
# Add a method called get_animal_types to the Farm class. This method should return a sorted list of all the animal types (names) in the farm. With the example above, the list should be: ['cow', 'goat', 'sheep'].
# Add another method to the Farm class called get_short_info. This method should return the following string: “McDonald’s farm has cows, goats and sheep.”. The method should call the get_animal_types function to get a list of the animals.

class Farm:
   

    def __init__(self:object, owner:str, farm = {"cow": 0, "sheep": 0, "goat": 0} ) -> object:

        self.owner = owner
        self.farm = farm


    def get_info(self:object) -> None:
       
            
        for animal, num in self.farm.items():
            print(f"{animal}: {num}")
        

    def get_short_info(self:object) -> None:
       

        short_info = self.get_animal_types()

        print(f"{self.owner}'s farm has {short_info[0]}s, {short_info[1]}s, and {short_info[2]}s.")


    def add_animal(self:object, animal:str, num_added = 1):
      
        if animal in self.farm.keys():
            self.farm[animal] += num_added
        else:
            print(f"Sorry {self.owner} you don't have those animals in stock just by one before starting adding them !!")


    def get_animal_types(self:object) -> list:
     

        type_list = []

        for animal in self.farm.keys():
            type_list.append(animal)

        return type_list

macdonald = Farm("McDonald")
macdonald.add_animal('cow', 5)
macdonald.add_animal('sheep')
macdonald.add_animal('sheep')
macdonald.add_animal('goat', 12)
macdonald.get_info()
macdonald.get_short_info()