from exerciseXP import MenuItem


def load_manager():
    print ('MENU')
def shower_user_menu():
    input1 = input('''(a)Add an item 
                   (d) Delete an item
                   (v) View the menu
                   (x) Exit ''')
    if input1 == 'a':
        add_item_to_menu()
        
    if input1 == 'd':
        remove_item_from_menu()
    if input1 == 'v':
        MenuItem.get_by_name('Beef Stew')
    if input1 == 'x':
        
        # print(items)
        return 'Exit'
    else :
        while input1 != 'a' or 'd' or 'v' or 'x':
             input1= input('''(a)Add an item 
                   (d) Delete an item
                   (v) View the menu
                   (x) Exit''')
            

def add_item_to_menu():
    inputname= input('Gimme an item name')
    inputprice= input('Gimme a price')
    inputprice = int(inputprice)
    item = MenuItem(inputname,inputprice)
    item.save()
def remove_item_from_menu():
    inputremove = input('input the name you want to remove from the restaurant menu')
    item = MenuItem(inputremove)
    item.delete(inputremove)
def show_restaurant_menu():
    return items


load_manager()
shower_user_menu()
# inputname= input('Gimme an item name')
# inputprice= input('Gimme a price')
# inputprice = int(inputprice)
# item = MenuItem(inputname,inputprice)
# add_item_to_menu()
# remove_item_from_menu()
# show_restaurant_menu()
# item.save()
# item.delete()
# item.update('Veggie Burger', 37)
# item2 = MenuItem.get_by_name('Beef Stew')
items = MenuItem.all()