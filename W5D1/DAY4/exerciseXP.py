# 🌟 Exercise 1 – Random Sentence Generator
# Instructions
# Description: In this exercise we will create a random sentence generator. We will do this by asking the user how long the sentence should be and then printing the generated sentence.

# Hint : The generated sentences do not have to make sense.

# Download this word list

# Save it in your development directory.

# Create a function called get_words_from_file. This function should read the file’s content and return the words as a collection. What is the correct data type to store the words?

# Create another function called get_random_sentence which takes a single parameter called length. The length parameter will be used to determine how many words the sentence should have. The function should:
# use the words list to get your random words.
# the amount of words should be the value of the length parameter.

# Take the random words and create a sentence (using a python method), the sentence should be lower case.

# Create a function called main which will:

# Print a message explaining what the program does.

# Ask the user how long they want the sentence to be. Acceptable values are: an integer between 2 and 20. Validate your data and test your validation!
# If the user inputs incorrect data, print an error message and end the program.
# If the user inputs correct data, run your code.

import random
from typing import final



def get_words_from_file(file):
    with open(file) as f:
        
        word_list = f.readlines()
        word_list = [word.replace('\n'," ") for word in word_list]
        print( word_list)

def get_random_sentence(file,length):
    with open(file) as f:
        word_list = f.readlines()
        word_list = [word.replace('\n'," ") for word in word_list]
        randomlist = random.choices(word_list,k=length)
        print(randomlist)
        
        list = []
            
         

def main (file):
    print ('The program is made to generate random word')
    user1 = input('How long you want the sentence to be , input a number between 2 and 20')

    get_random_sentence(file,int(user1))
    if int(user1) !=int:
      raise ValueError("You needed to write a number fool")
      
    else:
      pass



        
       
        

    


link = '/Users/benisti/Desktop/DI_Bootcamp_Stage1/W5D1/DAY4/ran.txt'
get_words_from_file(link)
get_random_sentence(link,4)
res = main(link)


# 🌟 Exercise 2: Working With JSON
# Instructions
import json
sampleJson = """{ 
   "company":{ 
      "employee":{ 
         "name":"emma",
         "payable":{ 
            "salary":7000,
            "bonus":800
         }
      }
   }
}"""
aDict = json.loads(sampleJson)
print(type(aDict))
print (aDict["company"]['employee']['payable']['salary'])
birth_date = aDict["company"]['employee']

birth_date1 = 'birth_date: 1996'
birth_date['Date_of_birth'] = 1996
print(birth_date)
print (aDict)
json_file = "my_file.json"
with open(json_file,'w') as file:
    json.dump(aDict,file)





