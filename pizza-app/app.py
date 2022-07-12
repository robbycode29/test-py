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

def choose_ingredients(pizza):
    print('1. Add ingredient')
    print('2. Remove ingredient')
    print('3. Finish')
    choice = input('Choose action: ')
    if choice == '1':
        ingredient_name = input('Ingredient name: ')
        ingredient_quantity = float(input('Ingredient quantity: '))
        ingredient_price_per_unit = float(input('Ingredient price per unit: '))
        ingredient = Ingredient(ingredient_name, ingredient_price_per_unit, quantity=ingredient_quantity)
        pizza.add_ingredient(ingredient)
        choose_ingredients(pizza)
    elif choice == '2':
        pizza.remove_ingredient(ingredient)
        choose_ingredients(pizza)
    elif choice == '3':
        pass
    else:
        pass


def menu():
    print('Order a pizza:')
    print('1. Margerita')
    print('2. Salami')
    print('3. Capricciosa')
    print('4. Custom')
    print('5. See past orders')
    print('6. Clear records')
    print('7. Add ingredient to cookbook')
    print('8. Remove ingredient from cookbook')
    print('9. Exit')
    return input('Your choice: ')



if __name__ == '__main__':
       
    while True:
        choice = menu()
        if choice == '1':
            pizza = order_pizza('margerita')
            choose_ingredients(pizza)
            save_pizza(pizza)
            print("Pizza: " + pizza.name)
            print("Price: " + str(pizza.price) + " RON")
        elif choice == '2':
            pizza = order_pizza('salami')
            choose_ingredients(pizza)
            save_pizza(pizza)
            print("Pizza: " + pizza.name)
            print("Price: " + str(pizza.price) + " RON")
        elif choice == '3':
            pizza = order_pizza('capricciosa')
            choose_ingredients(pizza)
            save_pizza(pizza)
            print("Pizza: " + pizza.name)
            print("Price: " + str(pizza.price) + " RON")
        elif choice == '4':
            pizza = order_pizza('custom_pizza')
            choose_ingredients(pizza)
            save_pizza(pizza)
            print("Pizza: " + pizza.name)
            print("Price: " + str(pizza.price) + " RON")
        elif choice == '5':
            print("Past orders: ")
            fetch_records()
            for pizza in Pizza.records:
                print((pizza['id'], str(pizza['name']), str("{}".format(pizza['price']) + " RON"), str(pizza['date'])))
        elif choice == '6':
            Pizza.clear_records()
        elif choice == '7':
            ingredient_name = input('Ingredient name: ')
            ingredient_price_per_unit = float(input('Ingredient price per unit: '))
            ingredient_quantity = float(input('Ingredient quantity: '))
            ingredient = Ingredient(ingredient_name, ingredient_price_per_unit, quantity=ingredient_quantity)
            ingredient.save_record()
        elif choice == '8':
            Ingredient.load_records()
            print("Ingredients:")
            for ingredient in Ingredient.records:
                print((ingredient['id'], str(ingredient['name']), str("{} RON".format(ingredient['price_per_unit'])), ingredient['quantity'], str(ingredient['date'])))
            ingredient_id = input('Ingredient id: ')
            Ingredient.remove_record(ingredient_id)
        elif choice == '9':
            break
        else:
            pass