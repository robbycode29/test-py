from ingredient import Ingredient
from datetime import date
import json
import os

class Pizza():

    adaos = 2

    records = []

    def __init__(self, id, name, ingredients=[]):
        self.id = id
        self.name = name
        self.ingredients = ingredients
        self.date = date.today().strftime("%d/%m/%Y")
        self.price = 0

    def toJSON(self):
        return {
            "id": self.id,
            "name": self.name,
            "ingredients": [ingredient.toJSON() for ingredient in self.ingredients],
            "date": self.date,
            "price": self.price
        }

    def record_JSON(self):
        return {
            "records": [
                record for record in self.records
            ]
        }

    def deliver_pizza(self):
        pass

    def calculate_price(self):
        for ingredient in self.ingredients:
            self.price += ingredient.calculate_price()*(self.adaos+1)
        self.price = round(self.price, 2)
        return self.price

    def add_ingredient(self, ingredient):
        self.ingredients.append(ingredient)
        # for ingredient in Ingredient.records:
        #     if ingredient['id'] == int(id):
        #         self.ingredients.append(ingredient)

    def remove_ingredient(self, ingredient):
        self.ingredients.remove(ingredient)
        # for ingredient in self.ingredients:
        #     if ingredient['id'] == int(id):
        #         self.ingredients.remove(ingredient)
        #     else:
        #         pass

    def save_record(self):
        self.records.append(self.toJSON())
        with open('./db/pizzas.json', 'w') as f:
            json.dump(self.record_JSON(), f)

    @classmethod    
    def create_margerita(cls, id):
        blat_normal = Ingredient('blat_normal', 5, 0.15)
        topping = Ingredient('mozzarella', 10, 0.08)
        sos = Ingredient('tomato_sauce', 8, 0.05)
        standard_ingredients = [blat_normal, topping, sos]
        return Pizza(id, 'Margerita', standard_ingredients)

    @classmethod
    def create_salami(cls, id):
        blat_normal = Ingredient('blat_normal', 5, 0.15)
        topping = Ingredient('mozzarella', 10, 0.08)
        sos = Ingredient('tomato_sauce', 8, 0.05)
        salami = Ingredient('salami', 15, 0.1)
        standard_ingredients = [blat_normal, topping, sos, salami]
        return Pizza(id, 'Salami', standard_ingredients)

    @classmethod
    def create_capricciosa(cls, id):
        blat_normal = Ingredient('blat_normal', 5, 0.15)
        topping = Ingredient('mozzarella', 10, 0.08)
        sos = Ingredient('tomato_sauce', 8, 0.05)
        salami = Ingredient('salami', 15, 0.1)
        pepperoni = Ingredient('pepperoni', 20, 0.15)
        standard_ingredients = [blat_normal, topping, sos, salami, pepperoni]
        return Pizza(id, 'Capricciosa', standard_ingredients)

    @classmethod
    def create_custom_pizza(cls, id):
        return Pizza(id, 'Custom')

    def save_to_file(self):
        with open('./db/{}.json'.format(self.name + str(self.id)), 'a') as f:
            json.dump(self.toJSON(), f)
            f.write('\n')

    @classmethod
    def load_from_file(cls):
        with open('./db/pizzas.json', 'r') as f:
            pizzas = json.load(f)
            return pizzas

    @classmethod
    def clear_records(cls):
        with open('./db/pizzas.json', 'w') as f:
            json.dump({}, f)
        path_to_file = './db/'
        for filename in os.listdir(path_to_file):
            if filename.endswith('.json') and filename != 'pizzas.json' and filename != 'ingredients.json':
                os.remove(path_to_file + filename)
        Pizza.records = []

      