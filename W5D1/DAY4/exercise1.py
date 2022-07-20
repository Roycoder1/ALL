# from cgitb import text


# file_text = ''
# text_lines =[]


# with open('./names.txt', mode="r") as f:
#     file_text+=f.read()
#     f.seek(0)
#     text_lines = f.readlines()
# print (text_lines)

# for line in enumerate(text_lines):
#     print (line)

# print (file_text[:5])

# print (text_lines[4])



# strip_newLine = lambda s:s.strip('\n')
# text_lines = list(map(strip_newLine,text_lines))
# names_uniques = set(text_lines)
# print (names_uniques)

# #First method
# # count_names = {name:0 for name in names_uniques}
# # print (count_names)
# # for name in text_lines:
# #     count_names[name]+=1

# # print(count_names)

# #Second method Easier

# from collections import Counter

# count_names = Counter(text_lines)
# print (count_names)
# print (count_names['Lea'])

# with open ('./names.txt',mode='a') as f:
#     f.write('\nRoy')


# for i, name in enumerate(text_lines):
#     if name=="Luke":
#         text_lines[i]+=' Skywalker'


# print (text_lines)

# with open ('./names.txt',mode='w') as f:
#     for line in text_lines:
#         f.write(line + '\n')

# requests.get('api_link')

import requests

response = requests.get('https://api.chucknorris.io/jokes/random')
print (response)
