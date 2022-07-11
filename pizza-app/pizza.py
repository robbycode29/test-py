from ingredient import Ingredient

class Pizza():

    adaos = 2

    def __init__(self, id, name, date, ingredients=[]):
        self.id = id
        self.name = name
        self.ingredients = ingredients
        self.date = date
        self.price = 0

    def __str__(self):
        return f"{self.id} {self.name} {self.ingredients} {self.date} {self.price}"

    def __repr__(self):
        return f"{self.id} {self.name} {self.ingredients} {self.date} {self.price}"


    def deliver_pizza(self):
        pass

    def calculate_price(self):
        for ingredient in self.ingredients:
            self.price += ingredient.calculate_price()*(self.adaos+1)
        return self.price

    @classmethod    
    def create_margerita(cls, id, date, custom_ingredients=[]):
        blat_normal = Ingredient('blat_normal', 5, 0.15)
        topping = Ingredient('mozzarella', 10, 0.08)
        sos = Ingredient('tomato_sauce', 8, 0.05)
        return Pizza(id, 'Margerita', date, custom_ingredients)

    @classmethod
    def create_salami(cls, id, date, custom_ingredients=[]):
        blat_normal = Ingredient('blat_normal', 5, 0.15)
        topping = Ingredient('mozzarella', 10, 0.08)
        sos = Ingredient('tomato_sauce', 8, 0.05)
        salami = Ingredient('salami', 15, 0.1)
        return Pizza(id, 'Salami', date, custom_ingredients)

    @classmethod
    def create_capricciosa(cls, id, date, custom_ingredients=[]):
        blat_normal = Ingredient('blat_normal', 5, 0.15)
        topping = Ingredient('mozzarella', 10, 0.08)
        sos = Ingredient('tomato_sauce', 8, 0.05)
        salami = Ingredient('salami', 15, 0.1)
        pepperoni = Ingredient('pepperoni', 20, 0.15)
        return Pizza(id, 'Capricciosa', date, custom_ingredients)

    @classmethod
    def create_custom_pizza(cls, id, date, custom_ingredients=[]):
        return Pizza(id, 'Custom', date, custom_ingredients)

    


