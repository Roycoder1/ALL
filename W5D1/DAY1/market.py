

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