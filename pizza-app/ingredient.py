class Ingredient():


    def __init__(self, name, price_per_unit, quantity=1, unit='kg'):
        self.name = name
        self.price_per_unit = price_per_unit
        self.quantity = quantity
        self.unit = unit

    def __str__(self):
        return f"{self.quantity} {self.unit} {self.name}"

    def __repr__(self):
        return f"Ingredient('{self.name}', {self.quantity}, '{self.unit}')"
    

    def calculate_price(self):
        return self.price_per_unit * self.quantity

 