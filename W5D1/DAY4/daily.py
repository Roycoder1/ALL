# First, we will analyze a simple string, like “A good book would sometimes cost as much as a good house.”

# Create a class called Text that takes a string as an argument and store the text in a attribute.
# Hint: You need to manually copy-paste the text, straight into the code

# Implement the following methods:
# a method to return the frequency of a word in the text (assume words are separated by whitespace) return None or a meaningful message.
# a method that returns the most common word in the text.
# a method that returns a list of all the unique words in the text.
from collections import Counter
from distutils import text_file
from pydoc import text




class Text():
    text = 'A good book would sometimes cost as much as a good house.'

    def __init__(self,string) -> None:
        self.string  = string

    def frequency(self):
        x = self.string.split(" ")
        count_names = Counter(x)
        print (count_names)
        return None
    def common(self):
        x = self.string.split(" ")
        count_names = Counter(x)
        common1 = count_names.most_common(2)
        print (common1)
    
    def unique(self):
        x = self.string.split(" ")
        unique1 = set(x)
        count_names = Counter(unique1)
        print(count_names)
    
    @classmethod
    def text_file(cls,file):
       
        with open(file) as f:
            readIt = f.readlines()
            read1=[word.replace('\n'," ") for word in readIt]
            print(read1)
            count_names = Counter(read1)






file= '/Users/benisti/Desktop/DI_Bootcamp_Stage1/W5D1/DAY4/stranger.txt'

result = Text(text)
# print(result.text)
# result.frequency()
# result.common()
# result.unique()
# result.text_file(text)
result2 = Text(file)
result2.frequency()
result2.common()
result2.unique
result2.text_file(file)

# Part II
# Then, we will analyze a text coming from an external text file. Download the_stranger.txt file.

# Implement a classmethod that returns a Text instance but with a text file:

#     >>> Text.from_file('the_stranger.txt')
# Hint: You need to open and read the text from the text file.


# Now, use the provided the_stranger.txt file and try using the class you created above.