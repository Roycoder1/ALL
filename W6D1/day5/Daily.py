import requests
import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT # <-- ADD THIS LINE
import json
HOSTNAME = 'localhost'
USERNAME = 'postgres'
PASSWORD = 'Azerty1234567890'
DATABASE = 'api'


connection = psycopg2.connect(host = HOSTNAME , user = USERNAME , password = PASSWORD,database = DATABASE)


# connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT) # <-- ADD THIS LINE
cursor = connection.cursor()
# query = "CREATE DATABASE api "
# cursor.execute(query)
# connection.commit()
# query2 = """create table COUNTRY(
#  id serial primary key,
#  name varchar(100),
#  capital varchar(50),
#  flag int,
#  subregion varchar(100),
#  population float
#  );   """
# cursor.execute(query2)
# connection.commit()
# connection.close()
# cursor.close()

nameapi = requests.get("https://restcountries.com/v3.1/name/united")
print (type(nameapi.text))
json1= json.loads(nameapi.text)
print (json1)
print (type(json1))
common = json1[0]["name"]['common']
# print (common)
capital = json1[0]["capital"]
print(capital)
flag = json1[0]["flags"]
print(flag)
subregion = json1[0]["subregion"]
print (subregion)
region = json1[0]["region"]
print (region)
population = json1[0]["population"]
print (population)





# print(nameapi.text)

name = f'INSERT INTO COUNTRY (name , capital, flag, subregion, population) VALUES ("{common}","{capital}","{flag}","{subregion}","{population}")'

cursor.execute(name)
connection.commit()
