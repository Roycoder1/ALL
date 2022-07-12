# 🌟 Exercise 1 : Convert Lists Into Dictionaries
# Instructions
# Convert the two following lists, into dictionaries.
# Hint: Use the zip method
# keys = ['Ten', 'Twenty', 'Thirty']
# values = [10, 20, 30]

# list1 = list(zip(keys,values))
# print(list1)

# 🌟 Exercise 2 : Cinemax
# Instructions
# A movie theater charges different ticket prices depending on a person’s age.
# if a person is under the age of 3, the ticket is free.
# if they are between 3 and 12, the ticket is $10.
# if they are over the age of 12, the ticket is $15.

# Given the following object:

# family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}


# How much does each family member have to pay ?

# Print out the family’s total cost for the movies.
# Bonus: Ask the user to input the names and ages instead of using the provided family variable (Hint: ask the user for names and ages and add them into a family dictionary that is initially empty).

from curses import has_key
from multiprocessing.sharedctypes import Value


family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}
price = 0
# value = []
# age = family.values()
# print(age)

for name, age in family.items():
    # age1 = int(f'{age}s is more')
    if age<3 :
        price += 0
    elif 3<=age<=12:
        price += 10
    else :
        price +=15
print(f'The final price of the movie for the family is {price}')

#  Exercise 3: Zara

 


# 2. Create a dictionary called brand which value is the information from part one (turn the info into keys and values).
# 3. Change the number of stores to 2.
# 4. Print a sentence that explains who Zaras clients are.
# 5. Add a key called country_creation with a value of Spain.
# 6. Check if the key international_competitors is in the dictionary. If it is, add the store Desigual.
# 7. Delete the information about the date of creation.
# 8. Print the last international competitor.
# 9. Print the major clothes colors in the US.
# 10. Print the amount of key value pairs (ie. length of the dictionary).
# 11. Print the keys of the dictionary.
# 12. Create another dictionary called more_on_zara with the following details:


brand = {
    "name": "Zara" ,
    "creation_date": 1975 ,
    "creator_name": "Amancio Ortega Gaona",
    "type_of_clothes" : ["men", "women", "children", "home"] ,
    "international_competitors": ["Gap", "H&M", "Benetton"], 
    "number_stores": 7000,
    "major_color" :{
        "France" : "blue", 
        "Spain": "red", 
        "US": "pink , green",
    }
}
brand["number_stores"] = 2
print(brand)
print(f'{brand["name"]} clients are childrens mens and womans ')
brand["country_creation"] = "Spain"
print(brand)
brandComp = "international_competitors"
brands = "Desigual"
print(brandComp)
if brandComp in brand:
    
    brand["international_competitors"] = "Gap", "H&M", "Benetton", "Desigual",
else :
    print("ahah")

    # for name,element in 
print(brand)
brand.pop("creation_date")
print(brand)
print(brand["international_competitors"][3])

print (brand["major_color"]["US"])
for key in brand :
    print("key", key)
    print(len(key))

print(brand.keys)

more_on_zara = {
    "creation_date": "1975", 
    "number_stores": "10 000",
    }


brand.update(more_on_zara)
print(brand)
print(brand["number_stores"])
# Overwrite the previous value

# Exercise 4 : Disney Characters

users = ["Mickey","Minnie","Donald","Ariel","Pluto"]

for index , value in enumerate(users)  :
    print (index,value)
    
for index , value in enumerate(users)  :
    print (value,index)

for index , value in enumerate(users)  :
    print (f'{value}:{index}')

print([x for x in users if "i" in x])

   