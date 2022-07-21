from math import perm
from anagram_checker import AnagramChecker

print(""""
Anagram menu
You will not be disapointed
""")

def menu():
    entry = input("input a word or exit")
    if entry !='exit':
        word = input ("Gimme a word ")
        word2 = input ("Gimme a word ")
        anagram = AnagramChecker()
        anagram.get_anagrams(word,word2)
        
    else :
        return
      
        







menu()
# word = input ("Gimme a word ")
# word2 = input ("Gimme a word ")
