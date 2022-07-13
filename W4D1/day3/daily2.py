text = input('gimme a sentence')
cypher_text = ''
for letter in text:
    cypher_text += chr(ord(letter) + 3)
    print (cypher_text)

encode = cypher_text
for letter in text:
    cypher_text += chr(ord(letter))
    print (cypher_text)
