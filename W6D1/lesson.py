import psycopg2


HOSTNAME = 'localhost'
USERNAME = 'postgres'
PASSWORD = 'Azerty1234567890'
DATABASE = 'dvdrental'

connection = psycopg2.connect(host = HOSTNAME , user = USERNAME , password = PASSWORD,database = DATABASE)
try:
    connection = psycopg2.connect(host = HOSTNAME , user = USERNAME , password = PASSWORD,database = DATABASE)
except:
    print ('Connection failed')

cursor = connection.cursor()

query = "select * from film"
cursor.execute(query)

results = cursor.fetchall()
print(results)
# for item in results:
#     print(item)

connection.close()