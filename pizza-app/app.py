from types import NoneType
from pizza import Pizza



def order_pizza(pizza_type, preferences=None):
    pizza = create_pizza(pizza_type)
    return pizza

def create_pizza(pizza_type):
    if pizza_type == 'margerita':
        return Pizza.create_margerita(id, date)
    elif pizza_type == 'salami':
        return Pizza.create_salami(id, date)
    elif pizza_type == 'capricciosa':
        return Pizza.create_capricciosa(id, date)
    elif pizza_type == 'custom_pizza':
        return Pizza.create_custom_pizza(id, date, custom_ingredients)
    else:
        raise ValueError('Invalid pizza type')



if __name__ == '__main__':
    pass