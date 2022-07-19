
from func import *
import random
import string
import datetime
from datetime import date

# 🌟 Exercise 2: Random Module
# Instructions
# Create a function that accepts a number between 1 and 100, then rolls a random number between 1 and 100,
# if it’s the same number, display a success message to the user, else don’t.

def randomNumber():
    
    randomNumber = random.randint(0,100)
    print(randomNumber)

    if random == sum2:
        print("Congrats you sucessed")
    else:
        print("wrong answer")

randomNumber()
print(sum2)

# 🌟 Exercise 3: String Module
# Instructions
# Generate random String of length 5
# Note: String must be the combination of the UPPER case and lower case letters only. No numbers and a special symbol.
# Hint: use the string module

def randomString(length):
    randomString = ''.join(random.choice(string.ascii_letters)for i in range(5))
    print(randomString)


        

randomString(5)
randomString(5)

# 🌟 Exercise 4 : Current Date
# Instructions
# Create a function that displays the current date.
# Hint : Use the datetime module.

x = datetime.datetime.now()
print(x)

# Exercise 5 : Amount Of Time Left Until January 1st
# Instructions
# Create a function that displays the amount of time left from now until January 1st.
# (Example: the 1st of January is in 10 days and 10:34:01hours).
now = date(2022,7,19)
nextYear = date(2023,1,1)
timeLast = nextYear-now
print (timeLast.days)

# Exercise 6 : Birthday And Minutes
# Instructions
# Create a function that accepts a birthdate as an argument (in the format of your choice), then displays a message stating how many minutes the user lived in his life.

def birthday(birth):
    a = birth
    print (a)
    b = datetime.datetime(2022,7,19 ,17,19,24)
    print(b)
    c = b-a
    print (c)
    minutes = divmod(c.total_seconds(),60)
    print(minutes)





res = birthday(datetime.datetime(1996,12,9,13,25,12))

# Exercise 7 : Upcoming Holiday
# Instructions
# Write a function that displays today’s date.
# The function should also display the amount of time left from now until the next upcoming holiday and print which holiday that is. (Example: the next holiday is in 30 days and 12:03:45 hours).
# Hint: Start by hardcoding the datetime and name of the upcoming holiday.

def today():
    today = datetime.datetime.now()
    today = date(2022,7,19)
    nextHoliday = date(2022,9,1)
    timeLastHoliday = nextHoliday-now
    return f' time until holiday{timeLastHoliday}'

vacation = today()
print(vacation)

# Exercise 8 : How Old Are You On Jupiter?
# Instructions
# Given an age in seconds, calculate how old someone would be on:
# Earth: orbital period 365.25 Earth days, or 31557600 seconds
# Mercury: orbital period 0.2408467 Earth years
# Venus: orbital period 0.61519726 Earth years
# Mars: orbital period 1.8808158 Earth years
# Jupiter: orbital period 11.862615 Earth years
# Saturn: orbital period 29.447498 Earth years
# Uranus: orbital period 84.016846 Earth years
# Neptune: orbital period 164.79132 Earth years
# So if you are told someone is 1,000,000,000 seconds old, the function should output that they are 31.69 Earth-years old.

ageInSeconds = 13468554*60 #minutes*60 to have the seconds
ageInDay = 13468554/60/24
print(ageInDay)
Earth = 31557600
difference = ageInSeconds/Earth
print (f'age on earth:{difference}')

Mercury = 0.2408467
DayMercury = 0.2408467*30*12
differenceMercury = ageInDay/DayMercury
print (f'age in mercury:{differenceMercury}')

Venus = 0.61519726
dayVenus = 0.61519726*30*12
differenceVenus = ageInDay/dayVenus
print (f'age in Venus:{differenceVenus}')

Mars = 1.8808158
dayMars = 1.8808158*30*12
differenceMars = ageInDay/dayMars
print (f'age in Mars:{differenceMars}')

Jupiter = 11.862615
dayJupiter = 11.862615*30*12
differenceJupiter = ageInDay/dayJupiter
print (f'age in Jupiter:{differenceJupiter}')

Saturn = 29.447498
daySaturn = 29.447498*30*12
differenceSaturn = ageInDay/daySaturn
print (f'age in Saturn:{differenceSaturn}')

Uranus = 84.016846
dayUranus = 84.016846*30*12
differenceUranus = ageInDay/dayUranus
print (f'age in Uranus:{differenceUranus}')

Neptune = 164.79132
dayNeptune = 164.79132*30*12
differenceNeptune = ageInDay/dayNeptune
print (f'age in Neptune:{differenceNeptune}')

# Exercise 9 : Faker Module
# Instructions
# Install the faker module, and take a look at the documentation and learn how to properly implement faker in your code.
# Create an empty list called users. Tip: It should be a list of dictionaries.
# Create a function that adds new dictionaries to the users list. Each user has the following keys: name, adress, langage_code. Use faker to populate them with fake data.





