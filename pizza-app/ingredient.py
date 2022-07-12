from datetime import date
import json

class Ingredient():

    records = []

    def __init__(self, name, price_per_unit, quantity=1, unit='kg'):
        self.id = self.get_id()
        self.name = name
        self.price_per_unit = price_per_unit
        self.quantity = quantity
        self.unit = unit
        self.date = date.today().strftime("%d/%m/%Y")

    def calculate_price(self):
        return self.price_per_unit * self.quantity

    def toJSON(self):
        return {
            "id": self.id,
            "name": self.name,
            "price_per_unit": self.price_per_unit,
            "quantity": self.quantity,
            "unit": self.unit,
            "date": self.date
        }
    
    @classmethod
    def record_JSON(self):
        return {
            "records": [
                record for record in self.records
            ]
        }

    @classmethod
    def load_records(cls):
        with open('./db/ingredients.json', 'r') as f:
            ingredients = json.load(f)
            cls.records = ingredients['records']

    def __repr__(self):
        return "{}".format(self.name)

    def get_id(self):
        if len(self.records) == 0:
            return 1
        else:
            return self.records[-1]['id'] + 1
    
    def save_record(self):
        self.records.append(self.toJSON())
        with open('./db/ingredients.json', 'w') as f:
            json.dump(self.record_JSON(), f)

    @classmethod
    def remove_record(cls, id):
        for record in cls.records:
            if record['id'] == int(id):
                cls.records.remove(record)
                with open('./db/ingredients.json', 'w') as f:
                    json.dump(cls.record_JSON(), f)

    def delete_records(self):
        self.records = []
        with open('./db/ingredients.json', 'w') as f:
            json.dump(self.records, f)