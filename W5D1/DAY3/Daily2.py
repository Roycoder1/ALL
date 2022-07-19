from googletrans import Translator,constants
from pprint import pprint
translator = Translator()

french_words= ["Bonjour", "Au revoir", "Bienvenue", "A bientôt"] 
# for i in french_words:
#     print(i)
#     translation1 = translator.translate(i,src= 'fr')
# print(translation1.text)

translation = translator.translate('Bonjour',src= 'fr')



translation2 = translator.translate('Au revoir',src= 'fr')



translation3 = translator.translate('Bienvenue',src= 'fr')



translation4 = translator.translate('A bientôt',src= 'fr')



french_words= [f'"Bonjour":{translation.text}, "Au revoir":{translation2.text}, "Bienvenue":{translation3.text}, "A bientôt":{translation4.text}']
print(french_words) 

