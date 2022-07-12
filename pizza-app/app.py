from pizza import Pizza
from ingredient import Ingredient
import json

def fetch_indices():
    with open('./db/pizzas.json', 'r') as f:
        try:
            pizzas = json.load(f)
            for pizza in pizzas['records']:
                id = pizza['id']
        except:
            id = 0
    return id

def fetch_records():
    with open('./db/pizzas.json', 'r') as f:
        try:
            pizzas = json.load(f)
            Pizza.records = pizzas['records']
        except:
            print('No records')

def save_pizza(pizza):
    pizza.calculate_price()
    pizza.save_to_file()
    pizza.save_record()

def order_pizza(pizza_type):
    id = int(fetch_indices()) + 1
    pizza = create_pizza(id, pizza_type)
    return pizza

def create_pizza(id, pizza_type):
    if pizza_type == 'margerita':
        return Pizza.create_margerita(id)
    elif pizza_type == 'salami':
        return Pizza.create_salami(id)
    elif pizza_type == 'capricciosa':
        return Pizza.create_capricciosa(id)
    elif pizza_type == 'custom_pizza':
        return Pizza.create_custom_pizza(id)
    else:
        raise ValueError('Invalid pizza type')

#######################################################################################################################
####                                                    Menus                                                     #####

def choose_ingredients(pizza):
    ingredients_to_be_added = []
    Ingredient.load_records()
    while True:
        print ("Extra ingredients:")
        if len(ingredients_to_be_added) != 0:
            for ingredient in ingredients_to_be_added:
                print("{}. {}".format(ingredient['id'], ingredient['name']))
        else:
            print("No extra ingredients")
        print("Would you like to add an extra ingredient?")
        print('1. Add ingredient')
        print('2. Remove ingredient')
        print('3. Finish')
        choice = input('Choose action: ')
        if choice == '1':
            print ('Available ingredients:')
            for ingredient in Ingredient.records:
                print((ingredient['id'], str(ingredient['name'])))
            choice = input('Add ingredient number: ')
            ingredients_to_be_added.append(Ingredient.records[int(choice) - 1])
            for ingredient in ingredients_to_be_added:
                pizza.add_ingredient(ingredient)
        elif choice == '2':
            print ('Available ingredients:')
            for ingredient in Ingredient.records:
                print((ingredient['id'], str(ingredient['name'])))
            choice = input('Remove ingredient number: ')
            for ingredient in ingredients_to_be_added:
                if ingredient['id'] == int(choice):
                    ingredients_to_be_added.remove(ingredient)
                    pizza.remove_ingredient(ingredient)
            pizza.remove_ingredient(choice)
        elif choice == '3':
            break
        else:
            break

def admin_interface():
    print('Manage:')
    print('1. See past orders')
    print('2. Clear records')
    print('3. Add ingredient to cookbook')
    print('4. Remove ingredient from cookbook')
    print('5. Exit')
    return input('Your choice: ')


def customer_interface():
    print('Welcome to the pizza shop!')
    print('1. Order a pizza')
    print('2. See order history')
    print('3. Exit')
    return input('Your choice: ')

def menu():
    while True:
        print('Our menu: ')
        print('1. Margerita')
        print('2. Salami')
        print('3. Capricciosa')
        print('4. Make your own')
        print('5. close menu')
        choice = input('Your choice: ')
        if choice == '1':
            pizza = order_pizza('margerita')
            choose_ingredients(pizza)
            save_pizza(pizza)
        elif choice == '2':
            pizza = order_pizza('salami')
            choose_ingredients(pizza)
            save_pizza(pizza)
        elif choice == '3':
            pizza = order_pizza('capricciosa')
            choose_ingredients(pizza)
            save_pizza(pizza)
        elif choice == '4':
            pizza = order_pizza('custom_pizza')
            choose_ingredients(pizza)
            save_pizza(pizza)
        elif choice == '5':
            break   

def order_history():
    fetch_records()
    for pizza in Pizza.records:
        print((pizza['id'], str(pizza['name']), str("{}".format(pizza['price']) + " RON"), str(pizza['date'])))

def customer_menu():
    while True:
        choice = customer_interface()
        if choice == '1':
            menu()
        elif choice == '2':
            order_history()
        elif choice == '3':
            break

def admin_menu():
    while True:
        choice = admin_interface()
        if choice == '1':
            print("Past orders: ")
            fetch_records()
            for pizza in Pizza.records:
                print((pizza['id'], str(pizza['name']), str("{}".format(pizza['price']) + " RON"), str(pizza['date'])))
        elif choice == '2':
            Pizza.clear_records()
        elif choice == '3':
            ingredient_name = input('Ingredient name: ')
            ingredient_price_per_unit = float(input('Ingredient price per unit: '))
            ingredient_quantity = float(input('Ingredient quantity: '))
            ingredient = Ingredient(ingredient_name, ingredient_price_per_unit, quantity=ingredient_quantity)
            ingredient.save_record()
        elif choice == '4':
            Ingredient.load_records()
            if len(Ingredient.records) == 0:
                print('No ingredients')
            else:
                print("Ingredients:")
                for ingredient in Ingredient.records:
                    print((ingredient['id'], str(ingredient['name']), str("{} RON".format(ingredient['price_per_unit'])), ingredient['quantity'], str(ingredient['date'])))
                ingredient_id = input('Ingredient id (type "none" to esc): ')
                if ingredient_id == 'none':
                    pass
                else:
                    Ingredient.remove_record(ingredient_id)
        elif choice == '5':
            break
        else:
            pass

if __name__ == '__main__':

    while True:
        print("1. Log in as admin")
        print("2. Log in as customer")
        print("3. Exit")
        choice = input("Your choice: ")
        if choice == "1":
            print("Admin")
            admin_menu()
        elif choice == "2":
            print("Customer")
            customer_menu()
        elif choice == "3":
            break
            



       
