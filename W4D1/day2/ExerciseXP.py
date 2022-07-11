# # 🌟 Exercise 1 : Set
# # Instructions
# # Create a set called my_fav_numbers with all your favorites numbers.
# # Add two new numbers to the set.
# # Remove the last number.
# # Create a set called friend_fav_numbers with your friend’s favorites numbers.
# # Concatenate my_fav_numbers and friend_fav_numbers to a new variable called our_fav_numbers.

# my_fav_numbers={3,9,12,18,24,33}
# my_fav_numbers.add(22)
# my_fav_numbers.add(49)
# print(my_fav_numbers)
# my_fav_numbers.pop()
# print(my_fav_numbers)
# friend_fav_numbers = {1,3,5,4,2}

# our_fav_numbers =my_fav_numbers.union(friend_fav_numbers)
# print(our_fav_numbers)

# # Exercise 2 :
# # Instructions
# # Given a tuple which value is integers, is it possible to add more integers to the tuple?

# # We can't to add more integers to a tuple but if we concatenate two tuples we can add integers
# # tuple1 = (1,3,5)
# # tuple2 = (4,9)
# # tuple1 = tuple1+tuple2
# # print(tuple1)


# # EXERCISE 3 :

# # Using this list basket = ["Banana", "Apples", "Oranges", "Blueberries"];

# # Remove “Banana” from the list.
# # Remove “Blueberries” from the list.
# # Add “Kiwi” to the end of the list.
# # Add “Apples” to the beginning of the list.
# # Count how many apples are in the basket.
# # Empty the basket.
# # Print(basket)

# basket = ["Banana", "Apples", "Oranges", "Blueberries"]

# basket.remove("Banana")
# print(basket)
# basket.remove("Blueberries")
# basket.append("Kiwi")
# basket.append("Apples")
# print(basket.count("Apples"))
# basket.clear()
# print(basket)

# # Exercise 4 :

# # Recap – What is a float? What is the difference between an integer and a float?
# # Can you think of another way to generate a sequence of floats?
# # Create a list containing the following sequence 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5 (don’t hard-code the sequence).

# # The difference between an integer and a float is that an integer is a decimal number and float is used to be more precise and give numbers after coma 


# # Another option to produce a range of floats is to use the NumPy module's arange() function. Where: start is the starting value of the range. stop specifies the end of the range.

# # list =[]
# # num = 1
# # for i in range (8):
# #     num +=0.5
   

# #     list.append(num)
# # print(list)

# # Exercise 5 :
# # 🌟 Exercise 5: For Loop
# # Instructions
# # Use a for loop to print all numbers from 1 to 20, inclusive.
# # Using a for loop, that loops from 1 to 20(inclusive), print out every element which has an even index.

# # for i in range (1,21):
# #     print(i)
      
  
# # for i in range (1,21):
# #     print(i)
# #     if i %2 == 1:
# #           print ('even')

# # Exercise 6:

# # Write a while loop that will continuously ask the user for their name, unless the input is equal to your name.


# # while True:
# #     user = input("Gimme your name")
# #     if user == 'roy':
# #         break
# # print('sucess')

# # 🌟 Exercise 7: Favorite Fruits
# # Instructions
# # Ask the user to input their favorite fruit(s) (one or several fruits).
# # Hint : Use the built in input method. Ask the user to separate the fruits with a single space, eg. "apple mango cherry".
# # Store the favorite fruit(s) in a list (convert the string of words into a list of words).
# # Now that we have a list of fruits, ask the user to input a name of any fruit.
# # If the user’s input is in the favorite fruits list, print “You chose one of your favorite fruits! Enjoy!”.
# # If the user’s input is NOT in the list, print, “You chose a new fruit. I hope you enjoy”.
# fav = input("What's your favorite fruit?")
# fruit_list = fav.split()
# print (fruit_list)
# userFav = input("Name of any fruit")
# if userFav==fav:
#     print('You chose one of your favorite fruits! Enjoy!')
# else:
# #         print('You chose a new fruit. I hope you enjoy')

# # Exercise 8:

# # Write a loop that asks a user to enter a series of pizza toppings, when the user inputs ‘quit’ stop asking for toppings.
# # As they enter each topping, print a message saying you’ll add that topping to their pizza.
# # Upon exiting the loop print all the toppings on the pizza pie and what the total price is (10 + 2.5 for each topping).


# # price = 10
# # list=[]
# # while True:

# #    toppings = input("Choose pizza toppings")
# #    if toppings != "quit":
# #         print(f"I will add {toppings } to your pizza") 
# #         price += 2.5
        
# #    else: 
# #        list.append(price)
# #        break


# # print (price)
# # print(list)

# # Exercise 9: Cinemax
# # Instructions
# # A movie theater charges different ticket prices depending on a person’s age.
# # if a person is under the age of 3, the ticket is free.
# # if they are between 3 and 12, the ticket is $10.
# # if they are over the age of 12, the ticket is $15.
# # Ask a family the age of each person who wants a ticket.
# # Store the total cost of all the family’s tickets and print it out.

# # A group of teenagers are coming to your movie theater and want to watch a movie that is restricted for people between the ages of 16 and 21.
# # Given a list of names, write a program that asks teenager for their age, if they are not permitted to watch the movie, remove them from the list.
# # At the end, print the final list.

# import numbers


# family= int(input("How many tickets do you want? "))


# for x in range(family):
#      print(x)
     
#      age = int(input("gimme your age?"))
#      if age < 3:

#       priceKid = 0
#       print (priceKid)

#       elif age >3 and age<=12 :
#      priceMedium = 10
#      print(priceMedium)

#      else : 
#      priceAdult = 15
#      print(priceAdult)

     # Exercise 10 :

sandwich_orders = ["Tuna sandwich", "Avocado sandwich", "Egg sandwich", "Sabih sandwich", "Pastrami sandwich"]
finished_sandwiches=[]

