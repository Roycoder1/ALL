import psycopg2


HOSTNAME = 'localhost'
USERNAME = 'postgres'
PASSWORD = 'Azerty1234567890'
DATABASE = 'Holywood'

# connection = psycopg2.connect(host = HOSTNAME , user = USERNAME , password = PASSWORD,database = DATABASE)
try:
    connection = psycopg2.connect(host = HOSTNAME , user = USERNAME , password = PASSWORD,database = DATABASE)
except:
    print ('Connection failed')


cursor = connection.cursor()

query = 'SELECT * FROM actors'
cursor.execute(query)

results = cursor.fetchall()
print (cursor.fetchall())
connection.commit()
connection.close()

