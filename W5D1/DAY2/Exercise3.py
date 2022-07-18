from ExerciseXP import Dog
import random

class PetDog(Dog):
    def __init__(self, name, age, weight) -> None:
        super().__init__(name, age, weight)
        self.trained = False
    
    def train (self):
        self.bark()
        self.trained = True
    
    def play(self,*args):
        self.args = args
        list=[self.args]
        print(list)
        print(f"{list} all play together")

    def trained_dog(self):
        sentence1 = [f"{self.name} does a barrel roll.",f"{self.name}  stands on his back legs.",f"{self.name}  shakes your hand.",f"{self.name}  plays dead."]
    
        Trained = True
        if Trained == True:
            print(random.choice(sentence1[0:3]))
            






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
laura = PetDog("Laura", 3,134)
laura.train()
laura.play("Regis",'foo',"baloulou")
laura.train()
laura.trained_dog()
