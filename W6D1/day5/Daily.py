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

json1= json.loads(nameapi.text)



# print(nameapi.text)

name = f'INSERT INTO COUNTRY (name,capital,flag,subregion,population) VALUES  '(())


# print (response.text)