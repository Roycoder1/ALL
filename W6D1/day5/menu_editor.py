from exerciseXP import MenuItem


def load_manager():
    print ('MENU')
def shower_user_menu():
    input = input('''(a)Add an item 
                   (d) Delete an item
                   (v) View the menu
                   (x) Exit''')
    if input == "a":
        item.save()
    if input == "d":
        item.delete()
    if input == "v":
        MenuItem.get_by_name('Beef Stew')
    if input == "x":
        print(items)
        return 'Exit'
    else :
        while input != "a" or "d" or "v" or "x":
             input('''(a)Add an item 
                   (d) Delete an item
                   (v) View the menu
                   (x) Exit''')

def add_item_to_menu():
    inputname= input('Gimme an item name')
    inputprice= input('Gimme a price')
    inputprice = int(inputprice)
    item.save(inputname,inputprice)
def remove_item_from_menu():
    inputremove = input('input the name you want to remove from the restaurant menu')
    item.delete(inputremove)
def show_restaurant_menu():
    print(items)

item = MenuItem('burger', 35)
# item.save()
# item.delete()
# item.update('Veggie Burger', 37)
# item2 = MenuItem.get_by_name('Beef Stew')
items = MenuItem.all()