from order import Order
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

def create_basic_ingredients():
    blat_normal = Ingredient('blat_normal', 5, 0.15)
    blat_normal.implicit = True
    blat_subtire = Ingredient('blat_subtire', 4, 0.15)
    blat_subtire.implicit = True
    blat_pufos = Ingredient('blat_pufos', 6, 0.15)
    blat_pufos.implicit = True
    topping = Ingredient('mozzarella', 10, 0.08)
    topping.implicit = True
    sos = Ingredient('tomato_sauce', 8, 0.05)
    sos.implicit = True
    salami = Ingredient('salami', 15, 0.1)
    salami.implicit = True
    pepperoni = Ingredient('pepperoni', 20, 0.15)
    pepperoni.implicit = True

    blat_normal_exists = False
    blat_subtire_exists = False
    blat_pufos_exists = False
    topping_exists = False
    sos_exists = False
    salami_exists = False
    pepperoni_exists = False
    for ingredient in Ingredient.records:
        if ingredient.name == 'blat_normal':
            blat_normal_exists = True
        if ingredient.name == 'blat_subtire':
            blat_subtire_exists = True
        if ingredient.name == 'blat_pufos':
            blat_pufos_exists = True
        if ingredient.name == 'mozzarella':
            topping_exists = True
        if ingredient.name == 'tomato_sauce':
            sos_exists = True
        if ingredient.name == 'salami':
            salami_exists = True
        if ingredient.name == 'pepperoni':
            pepperoni_exists = True
    
    if not blat_normal_exists:
        blat_normal.id = blat_normal.get_id()
        blat_normal.save_record()
    if not blat_subtire_exists:
        blat_subtire.id = blat_subtire.get_id()
        blat_subtire.save_record()
    if not blat_pufos_exists:
        blat_pufos.id = blat_pufos.get_id()
        blat_pufos.save_record()
    if not topping_exists:
        topping.id = topping.get_id()
        topping.save_record()
    if not sos_exists:
        sos.id = sos.get_id()
        sos.save_record()
    if not salami_exists:
        salami.id = salami.get_id()
        salami.save_record()
    if not pepperoni_exists:
        pepperoni.id = pepperoni.get_id()
        pepperoni.save_record()
   

######################################################################################################################
####                                                    Menus                                                     ####

def choose_ingredients(pizza):
    # if len(pizza.ingredients) != 0:
    #     ingredients_to_be_added = pizza.ingredients
    # else:
    #     ingredients_to_be_added = []
    while True:
        print ("Current ingredients:")
        if len(pizza.ingredients) != 0:
            for ingredient in pizza.ingredients:
                print("{}. {}, price per 1kg: {} RON".format(ingredient.id, ingredient.name, ingredient.price_per_unit))
            pizza.calculate_price()
            print("Total price: {} RON".format(pizza.price))
        else:
            print("No ingredients")

        print("Would you like to add an extra ingredient?")
        print('1. Add ingredient')
        print('2. Remove ingredient')
        print('3. Change crust')
        print('4. Finish')
        choice = input('Choose action: ')
        if choice == '1':
            print ('Available ingredients:')
            exists_available_ingredients = False
            for ingredient in Ingredient.records:
                if not ingredient.implicit:
                    print((ingredient.id, str(ingredient.name)))
                    exists_available_ingredients = True
                else:
                    pass
            if not exists_available_ingredients:
                print('No available ingredients')
            else:
                choice = input('Add ingredient number(s) separated by a comma (or type "none" to exit): ')
                choices = choice.split(',')
                for ingredient in Ingredient.records:
                    if str(ingredient.id) in choices:
                        is_ingredient_already_added = False
                        for item in pizza.ingredients:
                            if item.id == ingredient.id or item.name == ingredient.name:
                                print('Already added!')
                                is_ingredient_already_added = True
                            else: 
                                pass
                        if not is_ingredient_already_added:
                            pizza.add_ingredient(ingredient)
                    elif choice == 'none':
                        break
        elif choice == '2':
            print ('Available ingredients:')
            if len(pizza.ingredients) != 0:
                for ingredient in pizza.ingredients:
                    print((ingredient.id, str(ingredient.name)))
                choice = input('Remove ingredient number(s) separated by a comma (or "none" to exit): ')
                choices = choice.split(',')
                if choice == 'none':
                    pass
                else:
                    for ingredient in Ingredient.records:
                        if str(ingredient.id) in choices:
                            if ingredient.implicit:
                                print('Cannot remove implicit ingredient')
                            else:
                                pizza.remove_ingredient(ingredient)
            else:
                print('No ingredients')
        elif choice == '3':
            print ('Available crusts:')
            for ingredient in Ingredient.records:
                if ingredient.name == 'blat_normal' or ingredient.name == 'blat_subtire' or ingredient.name == 'blat_pufos':
                    print((ingredient.id, str(ingredient.name)))
            choice = input('Choose crust number: ')
            for ingredient in Ingredient.records:
                if ingredient.id == int(choice):
                    if ingredient.name == 'blat_normal' or ingredient.name == 'blat_subtire' or ingredient.name == 'blat_pufos':
                        pizza.change_crust(ingredient)
                    else:
                        print('Cannot change crust to this type')
        elif choice == '4':
            break
        else:
            break

def admin_interface():
    print('Manage:')
    print('1. See past orders')
    print('2. Clear records')
    print('3. Add ingredient to cookbook')
    print('4. Remove ingredient from cookbook')
    print('5. See all ingredients in cookbook')
    print('6. Exit')
    return input('Your choice: ')


def customer_interface():
    print('Welcome to the pizza shop!')
    print('1. Order a pizza')
    print('2. See order history')
    print('3. Go to shopping cart')
    print('4. Exit')
    return input('Your choice: ')

def add_to_cart(pizza):
    any_order_open = False
    for order in Order.orders:
        if order.status == True:
            order.add_pizza(pizza)
            order.save_order()
            any_order_open = True
        else:
            any_order_open = False
    
    if not any_order_open:
        order = Order([])
        order.add_pizza(pizza)
        order.save_order()


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
            add_to_cart(pizza)
        elif choice == '2':
            pizza = order_pizza('salami')
            choose_ingredients(pizza)
            save_pizza(pizza)
            add_to_cart(pizza)
        elif choice == '3':
            pizza = order_pizza('capricciosa')
            choose_ingredients(pizza)
            save_pizza(pizza)
            add_to_cart(pizza)
        elif choice == '4':
            pizza = order_pizza('custom_pizza')
            choose_ingredients(pizza)
            if len(pizza.ingredients) != 0:
                save_pizza(pizza)
                add_to_cart(pizza)
            else:
                print('Pizza couldn\'t be processed: No ingredients')
        elif choice == '5':
            break   

def order_history():
    if len(Order.orders) != 0:
        for order in Order.orders:
            print('Order number: {}'.format(order.order_id))
            print('Date: {}'.format(order.date))
            print('Status: {}'.format('closed' if not order.status else 'open'))
            print('Pizzas:')
            for pizza in order.pizzas:
                crust = ''
                for ingredient in pizza.ingredients:
                    if ingredient.name[:4] == 'blat':
                        crust = ingredient 
                print('{}. {}, crust type: {}'.format(pizza.id, pizza.name, crust.name))
            print('Total price: {}'.format(order.price))
            print('-----------------------------------------------------')
    else:
        print('No orders')
    # fetch_records()
    # for pizza in Pizza.records:
    #     print((pizza['id'], str(pizza['name']), str("{}".format(pizza['price']) + " RON"), str(pizza['date'])))

def shopping_cart(order):
    print('Your shopping cart:')
    for pizza in order.pizzas:
        print((pizza.id, str(pizza.name), str("{}".format(pizza.price) + " RON")))
    print('Total: ' + str("{}".format(sum(pizza.price for pizza in order.pizzas)) + " RON"))
    print('1. Pay')
    print('2. Remove pizza(s)')
    print('3. Exit')
    choice = input('Your choice: ')
    if choice == '1':
        print('Thank you for your order!')
        order.status = False
        order.save_order()
    elif choice == '2':
        choice = input('Remove pizza number(s) separated by a comma (or type "none" to cancel): ')
        choices = choice.split(',')
        if choice == 'none':
            pass
        else:
            pizzas_to_remove = []
            for pizza in order.pizzas:
                if str(pizza.id) in choices:
                    pizzas_to_remove.append(pizza)
                else:
                    pass
            for item in pizzas_to_remove:
                if item in order.pizzas:
                    order.pizzas.remove(item)
            order.save_order()
            print('Pizza(s) removed')
            if len(order.pizzas) == 0:
                order.remove_order()
    elif choice == '3':
        pass
    else:
        pass

def customer_menu():
    while True:
        choice = customer_interface()
        if choice == '1':
            menu()
        elif choice == '2':
            order_history()
        elif choice == '3':
            Order.load_orders()
            exists_open_order = False
            for order in Order.orders:
                if order.status == True:
                    shopping_cart(order)
                    exists_open_order = True
                else:
                    pass
            if exists_open_order == False:
                print('No items in shopping cart')
            
            # if len(Order.orders) == 0:
            #     print('Shopping cart empty!')
            # else:
            #     for order in Order.orders:
            #         if order.status == True:
            #             shopping_cart(order)
            #         else:
            #             pass
        elif choice == '4':
            break

def admin_menu():
    while True:
        choice = admin_interface()
        if choice == '1':
            print("Past orders: ")
            # fetch_records()
            # for pizza in Pizza.records:
            #     print((pizza['id'], str(pizza['name']), str("{}".format(pizza['price']) + " RON"), str(pizza['date'])))
            order_history()
        elif choice == '2':
            Pizza.clear_records()
            Order.clear_orders()
        elif choice == '3':
            ingredient_name = input('Ingredient name: ')
            ingredient_price_per_unit = float(input('Ingredient price per unit: '))
            ingredient_quantity = float(input('Ingredient quantity: '))
            ingredient = Ingredient(ingredient_name, ingredient_price_per_unit, quantity=ingredient_quantity)
            ingredient.save_record()
        elif choice == '4':
            if len(Ingredient.records) == 0:
                print('No ingredients')
            else:
                print("Ingredients:")
                for ingredient in Ingredient.records:
                    print((ingredient.id, str(ingredient.name), str("{} RON".format(ingredient.price_per_unit)), ingredient.quantity, str(ingredient.date)))
                ingredient_id = input('Ingredient id (type "none" to esc): ')
                if ingredient_id == 'none':
                    pass
                else:
                    Ingredient.remove_record(ingredient_id)
        elif choice == '5':
            if len(Ingredient.records) == 0:
                print('No ingredients')
            else:
                print("Ingredients:")
                for ingredient in Ingredient.records:
                    print((ingredient.id, str(ingredient.name), str("{} RON".format(ingredient.price_per_unit)), ingredient.quantity, str(ingredient.date)))
                    
        elif choice == '6':
            break
        else:
            pass

if __name__ == '__main__':

    Ingredient.load_records()

    create_basic_ingredients()

    Order.load_orders()

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
            



       
