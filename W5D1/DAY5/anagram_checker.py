import re
from collections import defaultdict
from itertools import permutations

class AnagramChecker():
    def __init__(self) -> None:
        pass
    def is_valid_word(self,word):
        res = "/[a-z]/gi"
        if word.isdigit():
            user = input ("Gimme a word ")
        else:
            return word
    def get_anagrams(self,word,word2):
        str1_list = list(word)
        str1_list.sort()
        str2_list = list(word2)
        str2_list.sort()
        print (str1_list == str2_list)
        anagramBool = (str1_list == str2_list)
        perm = list(permutations(word))
        print (perm)

        
        

            
word = input ("Gimme a word ")
word2 = input ("Gimme a word ")
anagram = AnagramChecker()
anagram.is_valid_word(word)
anagram.get_anagrams(word,word2)


