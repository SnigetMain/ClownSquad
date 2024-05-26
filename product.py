from dataclasses import dataclass

@dataclass
class Product:
    def __init__(self, name = '', price = 0, ingridients=[], additional=[[]], energy=0,cook_time=0):
        self.price = price
        self.name = name
        self.ingredients = ingridients
        self.energy_value = energy
        self.cooking_time = cook_time
        self.additional = additional