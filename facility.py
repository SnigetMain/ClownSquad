from product import Product
from order import Order, Status
from cooker import Cooker
from courier import Courier
from worker import WorkerStatus

Facilities = []

class Facility:

    list_cookers: list[Cooker]
    list_orders: list[Order]

    def __init__(self, start_time=(0, 0), end_time=(23, 59), name=''):
        self.name = name
        self.list_orders = []
        self.menu=[]
        self.list_cookers=[]
        self.workig_hours = (start_time, end_time)

    def add_dish(self):
        dish_name=input('Введите название блюда: ')
        dish_price=int(input('Введите цену блюда: '))
        dish_ingridients = map(str, input('Введите ингридиенты через пробел: ').split(' '))
        dish_additional=[()]
        dish_energy=input('Введите энергетическую ценность блюда: ')
        dish_price=input('Введите время приготовления блюда: ')
        count_of_aditional=int(input('Сколько допов для блюда? '))
        for i in range(count_of_aditional):
            a=input('Введите название допа: ')
            b=int(input('Введите цену допа: '))
            dish_additional.append((a,b))
        dish_time=int(input('Введите время приготовления: '))
        new_dish=Product(dish_name,dish_price,dish_ingridients, dish_additional,dish_energy,dish_time)
        self.menu.append(new_dish)

    def add_order(self, new_order :Order):
        new_order.status=Status.ACCEPTED
        self.list_orders.append(new_order)
        
    def add_cooker(self):
        new_cooker=Cooker(6)
        new_cooker.get_shift(0)
        self.list_cookers.append(new_cooker)

    def cooking_process(self):
        for order in self.list_orders:
            if order.status==Status.ACCEPTED:
                for cook in self.list_cookers:
                    if cook.workerStatus==WorkerStatus.FREE:
                        cook.give_order(order)
                        break
        for cook in self.list_cookers:
            if cook.workerStatus==WorkerStatus.INPROGRESSWORK:
                cook.order_assembly()
    
    def give_order(self, list_couriers :list[Courier]):
        for order in self.list_orders:
            if order.status==Status.INSTOCK:
                for courier in list_couriers:
                    if courier.workerStatus==WorkerStatus.FREE:
                        courier.give_order(order)
                        self.list_orders.remove(order)

def add_facility(start_time=(0, 0), end_time=(23, 59), name=''):
    Facilities.append(Facility(start_time, end_time, name))

add_facility(name='MacDac')
Facilities[0].menu = [
    Product('Burger', 100, ['bulka', 'cotleta', 'trava', 'bulka'], [
        ('negr', 10), ('ketchup', 20), ('mayo', 20) ], 200, 300),
    Product('FriedPotato', 400, ['potato', 'fire', 'another_potato'], [
        ('negr', 10), ('ketchup', 20), ('mayo', 20) ], 500, 600),
    Product('Coke', 400, ['smoke', 'wire', 'every', 'day'], [
        ('negr', 10), ('zona', 1000000000000), ('mayo', 20) ], 500, 600),    
]

