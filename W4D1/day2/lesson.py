# # # from itertools import product


# # # list = [1,2,3,4,5]




# # # # Index looping when looping from the middle
# # # print ("Looping through the indexes")
# # # # for i , val in enumerate(list):
# # # #     print(i)
# # # #     print(val)



# # # # enumerate for looping from the start of the list
# # # print("Looping with enumerates")
# # # for i in range (2 , len(list),2):
# # #     print(i)
# # #     print(list[i])


# # # for num in list[2:]:
# # #         print(num)

# # # product= list[0]
# # # # for num in list[1:]:
# # # #     product*=list[num]


# # # num = []
# # # num.append(1)
# # # print(num)

# # # num.insert(0,0)
# # # print(num)

# # # # PAR ELEMENT
# # # # num.remove(1)
# # # # print(num)

# # # # par index
# # # del num [0]
# # # print(num)


# # # num+=[2,3,4]
# # # num.pop()
# # # print(num)

# # # # pop for removing by index +returning
# # # eligible_users = ['yossi', 'david', 'reuven']
# # # blocked_user=eligible_users.pop(1)
# # # print(blocked_user)

# # # # SORTING ITEMS

# # # char_list = [ 'z','b', 'f', 'a']
# # # sort = sorted(char_list) 

# # from os import remove
# # from re import A


# # list1 = [5,10,15,20,25,50,20]

# # idx =list1.index(20)

# # print(idx)
# # list1[idx]=200
# # print(list1)

# # a= 5
# # b = 10
# # a , b = b , a
# # print(a,b)

# # # num1,num2,num3 = int(input('Gimme a number').split(','))
# # num1,num2,num3 = map(int,input('Gimme a number').split(','))
# # print('num1 : num1*10')

# # from multiprocessing.reduction import duplicate


# a_tuple = (10,20,30,40)
# print(a_tuple[0])
# print(a_tuple[1])
# print(a_tuple[2])
# print(a_tuple[3])

# # SETS

# a_set = {1,2,3,4}
# a_set=set({})
# print(type(a_set))

# duplicatesList = [1,1,1,1,2,2,'a','c']
# list_to_set = set(duplicatesList)
# print(list_to_set)

# colorsA ={'red' , 'green','blue', 'pink' }
# colorsB = {'grey', 'green', 'blue', 'yellow'}

# # intersection
# print('Intersection:' , colorsA & colorsB)

# print('Union:', colorsA| colorsB)

# print ('Without intersection :', colorsA ˆ colorsB)
# usernumber = int(input('Gimme a number'))

for i in range(1, 6):
     string =''
    
    for j in range(1, 11):
        string +=f'{i*j}|'
    print(string)

        
