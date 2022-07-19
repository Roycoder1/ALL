# Une méthode statique est une méthode qui n'obtient pas self.

class MyClass:
  @staticmethod
  def add(a, b): 
    return a + b

print(MyClass.add(3, 6))
# >> 9

@Classmethod
# Les méthodes de classe sont des méthodes qui ne sont pas liées à un objet mais à une classe. Son premier argument est la classe elle-même (rappelez-vous que les classes sont aussi des objets).

class MyClass:
  __counter = 0

  @classmethod
  def add(cls,a): 
    return cls.__counter + a

my_class_add = MyClass.add(3)
print(my_class_add)
# >> 3

new_class = MyClass()
new_class.__counter = 1

print(new_class.add(3))
# >> 3

# The output is still three because the method a

# 2. The __str__ Method
# The __str__ function is the function that python calls when it needs to convert an object to a string, for example, when printing it.

# For example:

mylist = [1, 3, 5]
print(str(mylist))

# 3. The __len__ Method
# The __len__ method is here to return the length of the object.
#  It’s the method that is called when you try to reach len(my_object).

# 4. The __call__ Method
# One of the essential unique methods will be used when you try to call the object (meaning adding () at the end of the name: my_object()).

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __call__(self):
        print ('Person: {}, Age: {}'.format(self.name, self.age))

person1 = Person("Sarah", 25)
person1()
# Person: Sarah, Age: 25

# 5. __repr__ And __str__
# Most classes should at least have these unique methods:

# object.__str__:
# Called by the str() built-in function and by the print function to compute the informal string representation of an object.
# __str__ will always be a string representation,



# object.__repr__:
# Called by the repr() built-in function to compute the official string representation of an object.
# __repr__ can be a more “behind the scenes” look at the object.

class Person:
  def __init__(self, name, age):
      self.name = name
      self.age  = age

  def __repr__(self):
      return f"{self.__class__.__name__} : {self.name} {self.age}"

newPerson = Person('Sarah', 24)

print(newPerson)
# >> Person : Sarah 24 
# __repr__ is the representation of an object
