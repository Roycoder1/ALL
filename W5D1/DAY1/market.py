class Farm (): #the farm class should be implemented with class and the name Farm 
    
    def __init__(self,farmName) -> None:#__init__ method is necessary for defining the name of the farm 
        self.farmName = farmName
        print(f"{self.farmName}'s farm")
        
    def add_animal(self,name,age):#Needs only add_animal method and get_info method
        self.name=name
        self.age= age
        
        print(f"{self.name}: {self.age}")
        
    
    def get_info(self):
        print("E-I-E-I-0")
    def get_animal_types(self):
       
        name1 = "cow"
        name2 = "sheep"
        name3 = "goat"
        listFarms = [name1,name2,name3]
        listFarms = sorted(listFarms)
        return listFarms
        
    def get_short_info(self):
        name1 = "cow"
        name2 = "sheep"
        name3 = "goat"
        listFarms = [name1,name2,name3]
        listFarms = sorted(listFarms)
        print(f"McDonald’s farm has{name1} {name2} and {name3} ")



macdonald = Farm("McDonald")
macdonald.add_animal('cow',5)
macdonald.add_animal('sheep',2)#It should have 2 elements otherwise it will be an error
macdonald.add_animal('goat', 12)
macdonald.get_info()
macdonald.get_animal_types()
macdonald.get_short_info()

# eXPAND THE Farm

