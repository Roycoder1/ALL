
from secrets import choice
import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT # <-- ADD THIS LINE
from psycopg2.extensions import AsIs

HOSTNAME = 'localhost'
USERNAME = 'postgres'
PASSWORD = 'Azerty1234567890'
DATABASE= 'exercisexp'


# connection = psycopg2.connect(host = HOSTNAME , user = USERNAME , password = PASSWORD)
# try:
#     connection = psycopg2.connect(host = HOSTNAME , user = USERNAME , password = PASSWORD,database = DATABASE)
# except:
#     print ('Connection failed')

# connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT) # <-- ADD THIS LINE
# cursor = connection.cursor()
# query = "CREATE DATABASE exerciseXP "
# cursor.execute(query)
# connection.commit()
# query2 = """create table menu_item(
#  id serial primary key,
#  item varchar(100),
#  price int);   """
# cursor.execute(query2)
# connection.commit()
# connection.close()
# cursor.close()

class MenuItem():
    def __init__(self, item, price) -> None:
        self.item = item
        self.price = price
        
    
    def runquery(self,query):
        connection = psycopg2.connect(host = HOSTNAME , user = USERNAME , password = PASSWORD,database = DATABASE)
        cursor = connection.cursor()
        cursor.execute(query)
        connection.commit()
        try:
            results = cursor.fetchall()
            connection.close()
            return results
        except:
            connection.close()
        
        
    def save(self):
        
        try:
            query = f"INSERT INTO menu_item (item, price) VALUES ('{self.item}', {self.price})"
            self.runquery(query)
        except:
            return False


        # cursor = connection.cursor()
        # insertion = 'INSERT INTO menu_item (item,price) values(%s,%s)'
        # val = (self.item,self.price)
        # cursor.execute(insertion,val)
        # # connection.close()
        # # cursor.close()

    def delete (self):

        try:
            deletion = f"DELETE FROM menu_item where item = '{self.item}'"
            self.runquery(deletion)
        except:
            return False

    def update(self,new_item , new_price):
        self.new_item = new_item
        self.new_price = new_price
        try:
            update_item = f" UPDATE menu_item SET item = '{self.new_item}' where item= {self.item} "
            self.runquery(update_item)
        except:
            return False
        

    def all(self):
        try:
            all = f"SELECT * FROM menu_item"
            MenuItem.runquery(self,all)
            print (MenuItem.runquery(self,all))
        except:
            return False

    def get_by_name(self):
        
        choice = input ('Choose an item ')
        user= f"SELECT * FROM menu_item where item = '{choice}'"
        res = MenuItem.runquery(self,user)
        return res
        # print (res)
            
        
            
item = MenuItem('burger', 35)
item.save()
item.delete()
item.update('Veggie Burger', 37)
item2 = MenuItem.get_by_name('Beef Stew')
print(item2)
items = item.all()
