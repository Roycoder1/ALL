# class Pets():
#     def __init__(self, animals):
#         self.animals = animals

#     def walk(self):
#         for animal in self.animals:
#             print(animal.walk())

# class Cat():
    
#     is_lazy = True

#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#     def sing(self, sounds):
#         return f'{sounds}'

#     def walk(self):
#         return f'{self.name} is just walking around'

# class Bengal(Cat):
#     pass

# class Chartreux(Cat):
#     pass

# class Siamese(Cat):
#     pass

# bengal = Bengal("Bob",1)
# chartreux = Chartreux("George",2)
# siamese = Siamese("sonia",5)

# all_cats = [bengal,chartreux,siamese]

# saras_pets = Pets(all_cats)

# saras_pets.walk()

# Exercise2 :
# Create a class called Dog with the following attributes name, age, weight.
# Implement the following methods in the Dog class:
# bark: returns a string which states: “<dog_name> is barking”.
# run_speed: returns the dogs running speed (weight/age*10).
# fight : takes a parameter which value is another Dog instance, called other_dog. This method returns a string stating which dog won the fight. The winner should be the dog with the higher run_speed x weight.

# Create 3 dogs and run them through your class.

class Dog ():
    
    def __init__(self,name,age,weight) -> None:
        self.name = name
        self.age = age
        self.weight=weight
    
    def bark (self):
         print(f"{self.name} is barking")

    def run_speed(self):
        power = self.weight/(self.age*10)
        return power 

    def fight(self,other_dog):
      running_speed = self.run_speed()
      if running_speed * self.weight > other_dog.run_speed() * other_dog.weight:
        print(f'{self.name} won the fight')
      else:
        print(f'{other_dog.name} won the fight')
    
dogBattle  = Dog("Rick",6,23)
print(dogBattle.name,dogBattle.age,dogBattle.weight)
dog2 = Dog("Henry",8,16)
dog3 = Dog("jim",4,7)
dogBattle.bark()
print(dogBattle.bark())
dogBattle.run_speed()
dog2.bark()
dog2.run_speed()
dog3.bark()
dog3.run_speed()
dogBattle.fight(dog3)
dog2.fight(dogBattle)
dog3.fight(dog2)
dog2.bark()

# 🌟 Exercise 3 : Dogs Domesticated
# Instructions
# Create a new python file and import your Dog class from the previous exercise.
# In the new python file, create a class named PetDog that inherits from Dog.
# Add an attribute called trained to the __init__ method, this attribute is a boolean and the value should be False by default.
# Add the following methods:
# train: prints the output of bark and switches the trained boolean to True

# play: takes a parameter which value is a few names of other Dog instances (use *args). The method should print the following string: “dog_names all play together”.

# do_a_trick: If the dog is trained the method should print one of the following sentences at random:
# “dog_name does a barrel roll”.
# “dog_name stands on his back legs”.
# “dog_name shakes your hand”.
# “dog_name plays dead”.



