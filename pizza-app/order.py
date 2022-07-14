import json
from ingredient import Ingredient
from pizza import Pizza

class Order():

    orders = []
    
    def __init__(self, pizzas=[]):
        self.order_id = self.get_id()
        self.pizzas = pizzas
        self.price = self.calculate_price()
        self.status = True

    def toJSON(self):
        return {
            "order_id": self.order_id,
            "pizzas": [pizza.toJSON() for pizza in self.pizzas],
            "price": self.calculate_price(),
            "status": self.status
        }
    
    @classmethod
    def order_JSON(cls):
        return {
            "orders": [
                order.toJSON() for order in cls.orders
            ]
        }

    @classmethod
    def db_dump(cls):
        with open('./db/orders.json', 'w') as f:
            json.dump(cls.order_JSON(), f)

    def save_order(self):
        order_is_in_list = False
        for order in self.orders:
            if order.order_id == self.order_id:
                order_is_in_list = True
            else:
                pass
        if order_is_in_list == False:
            Order.orders.append(self)
            Order.db_dump()
        else:
            Order.db_dump()

    @classmethod
    def load_orders(cls):
        cls.orders = []
        with open('./db/orders.json', 'r') as f:
            orders = json.load(f)
            if len(orders['orders']) == 0:
                pass
            else:
                for order in orders['orders']:
                    pizzas = []
                    for pizza in order['pizzas']:
                        ingredients = []
                        for ingredient in pizza['ingredients']:
                            new_ingredient = Ingredient(ingredient['name'], ingredient['price_per_unit'], ingredient['quantity'], ingredient['unit'])
                            new_ingredient.id = ingredient['id']
                            new_ingredient.date = ingredient['date']
                            ingredients.append(new_ingredient)
                        new_pizza = Pizza(pizza['id'], pizza['name'], ingredients)
                        new_pizza.price = pizza['price']
                        pizzas.append(new_pizza)
                    new_order = Order(pizzas)
                    new_order.order_id = order['order_id']
                    new_order.status = order['status']
                    new_order.price = order['price']
                    cls.orders.append(new_order)

    @classmethod
    def clear_orders(cls):
        cls.orders = []
        with open('./db/orders.json', 'w') as f:
            json.dump(cls.order_JSON(), f)
    
    def calculate_price(self):
        self.price = 0
        for pizza in self.pizzas:
            self.price += pizza.price
        return self.price
    
    def add_pizza(self, pizza):
        self.pizzas.append(pizza)
        self.save_order()

    def remove_pizza(self, pizza):
        self.pizzas.remove(pizza)
        self.save_order()

    def remove_order(self):
        Order.orders.remove(self)
        self.status = False
        self.save_order()

    def get_id(self):
        if len(self.orders) == 0:
            return 1
        else:
            return self.orders[-1].order_id + 1

