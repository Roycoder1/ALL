
from typing import List
from unicodedata import name


class Family ():
    def __init__(self,last_name , *members) -> None:
        self.members = members
        self.last_name = last_name
        list = []
        # list.append(self.members)
        # print(list)
        for i in self.members:
           list.append(i) 
           print(i)
    
    def born(self,*kwargs):
        self.kwargs = kwargs
        self.members = kwargs
        list=[]
        list.append(self.members) 
        print(list)
    
    # def is_18(self,last_name):
    #     self.last_name = last_name
    #     if self.age >=18:
    #         return True
    #     else:
    #         return False
    
    def family_presentation(self):
        pass
        print(self.members)
    
# Exercise 2:

class TheIncredibles(Family):
    def __init__(self, last_name, *members) -> None:
        super().__init__(last_name, *members)

    # def use_power():







        
        


list = []
list2 = []
family = Family("Miller",[{"name" :"Michael","age":35,"gender":"Male","is_child": False}])
sarah = Family("Miller",[{"name" :"Sarah","age":32,"gender":"Female","is_child": False}])
list.append(family)
list2.append(sarah)
list+=list2
print(list[0].members,list[1].members)

family.born("Miller",{"name" :"BabyShark","age":1,"gender":"Female","is_child": True})
# family.is_18("Miller")
incredibles = TheIncredibles("Miller",{"name" :"Sarah","age":32,"gender":"Female","is_child": False,"power":"fly","incredible_name":"Mike"})