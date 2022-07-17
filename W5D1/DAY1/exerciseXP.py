# class Cat:
#     cats = []
#     def __init__(self, cat_name, cat_age):
#         self.name = cat_name
#         self.age = cat_age
#         Cat.cats.append(self)
# cat1 = Cat("Roger" , 3)
# cat2 = Cat("Franck", 6)
# cat3 = Cat("Holishit", 12)




# def older(list) -> object:
#     old = list[0]
#     for i in list:
#       if i.age>old.age:
#         old = i
#     return old
# old = older(Cat.cats)
# print(old.name)
    
# print(f"Le chat le plus âgé est {old.name}, et a {old.age}ans.")

# Create a class called Dog.
# In this class, create an __init__ method that takes two parameters : name and height. This function instantiates two attributes, which values are the parameters.
# Create a method called bark that prints the following string “<dog_name> goes woof!”.
# Create a method called jump that prints the following string “<dog_name> jumps <x> cm high!”. x is the height*2.
# Outside of the class, create an object called davids_dog. His dog’s name is “Rex” and his height is 50cm.
# Print the details of his dog (ie. name and height) and call the methods bark and jump.
# Create an object called sarahs_dog. Her dog’s name is “Teacup” and his height is 20cm.
# Print the details of her dog (ie. name and height) and call the methods bark and jump.
# Create an if statement outside of the class to check which dog is bigger. Print the name of the bigger dog.

from tokenize import single_quoted
from unicodedata import name


class Dog():
    
    def __init__(self:object, name , height) -> None:
       self.name = name
       self.height = height
     
    def bark (self):
        print(self.name + "va woof")
    def jump(self):
        x = self.height * 2 
         
        print(f'{self.name} jumps {x} cm high')
Dog1 = Dog("Henry", 25)
Dog1.bark()
Dog1.jump()

DogRex = Dog("Rex", 20)
DogRex.bark()
DogRex.jump()
Sarah = Dog("Teacup",20)
Sarah.bark()
Sarah.jump()
doglist= [Dog1.height,DogRex.height,Sarah.height]
print(doglist)
bigger = Dog1
for i in doglist:
    if Dog1.height>DogRex.height:
        bigger = Dog1
print(bigger.height)
print(f'The bigger dog is {Dog1.name}')

# 🌟 Exercise 3 : Who’s The Song Producer?
# Instructions
# Define a class called Song, it will show the lyrics of a song.
# Its __init__() method should have two arguments: self and lyrics (a list).
# Inside your class create a method called sing_me_a_song that prints each element of lyrics on its own line.
# Create an object, for example:

class Song():
    def __init__(self,lyrics) -> None:
        self.lyrics = lyrics

    def sing_me_a_song(self):
        print(self.lyrics)

stairway= Song(["There’s a lady who's sure","all that glitters is gold", "and she’s buying a stairway to heaven"])
stairway.sing_me_a_song()


# Exercise 4 : Afternoon At The Zoo
# Instructions
# Create a class called Zoo.
# In this class create a method __init__ that takes one parameter: zoo_name.
# It instantiates two attributes: animals (an empty list) and name (name of the zoo).
# Create a method called add_animal that takes one parameter new_animal. This method adds the new_animal to the animals list as long as it isn’t already in the list.
# Create a method called get_animals that prints all the animals of the zoo.
# Create a method called sell_animal that takes one parameter animal_sold. This method removes the animal from the list and of course the animal needs to exist in the list.
# Create a method called sort_animals that sorts the animals alphabetically and groups them together based on their first letter.

class Zoo():
    
    def __init__(self,zoo_name) -> None:
       self.zoo_name = zoo_name
       self.animals = []
       
       
    def add_animal(self,new_animal):
        self.new_animal =new_animal 
        if new_animal != self.animals:
            self.animals.append(new_animal)
    def get_animal(self):
        print(self.new_animal)
    def sell_animal(self,animal_sold):
        self.animal_sold = animal_sold
        self.animals.remove(animal_sold)

    def sort_animals(self):
        self.animalsDictionnary = {}
        

        for idx in range (len(self.animals)):

            if self.animals[idx][0][0] not in self.animalsDictionnary:
                   self.animalsDictionnary[self.animals[idx][0]] = [self.animals[idx]]
        
            else:
                    self.animalsDictionnary[self.animals[idx][0]].append(self.animals[idx])
        x = sorted(self.animals)
        print(x)
    def get_groups(self):
        for i in self.animalsDictionnary:
            print(self.animalsDictionnary[i])
    


# { 
#     1: "Ape",
#     2: ["Baboon", "Bear"],
#     3: ['Cat', 'Cougar'],
#     4: ['Eel', 'Emu']
# }

        
       

anim = Zoo("Papaya") 
anim.add_animal("Zebra")
anim.add_animal("Snake")
anim.add_animal("Sheep")
anim.add_animal("Gorilla")
anim.add_animal("Bear")
anim.add_animal("Cat")
anim.sell_animal("Zebra")
print(anim.animals)
anim.sort_animals()
anim.get_groups()
add = anim.add_animal('Giraffe')
ramat_gan_safari = anim.add_animal("Giraffe"),anim.sell_animal("Cat"),anim.get_animal(),anim.sort_animals(),anim.get_groups()
print(f'Which animal should we {add} to the zoo')


print(anim.animalsDictionnary)





