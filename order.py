from dataclasses import dataclass
from enum import Enum
from product import Product
# from typing import List
from client import Client
from facility import Facility
import uuid

from dataclasses import dataclass
from enum import Enum
from product import Product
# from typing import List
import uuid


class Status(Enum):
    PROCESSING = 0  # обработка
    ACCEPTED = 1  # приянт
    INSTOCK = 2  # приготовление
    ONTHEWAY = 3  # в пути
    INPOINT = 4  # в пунткте
    RECEIVED = 5  # получен
    CANCEL = 6  # отменен


class Order:
    orderId: str
    status: Status
    ProductList: list[Product]
    timeCreation: tuple[int]
    address: str
    client: Client
    facility: Facility
    #collector: User
    

    # collector: User

    def __init__(self, status: Status = 0, ProductList: list[Product] = [], adress="", timeCreation=0):
        self.orderId = uuid.uuid1()
        self.client = client
        self.status = status
        self.facility = facilty
        self.ProductList = ProductList
        self.timeCreation = timeCreation
        self.address = adress
        # self.collector = collector

    def change_status(self, status: Status):
        self.status = status

    def printOrder(self):
        print(f'ID: {self.orderId}')
        print(f'Кому: {self.client.name}')
        print(f'Статус заказа: {self.status.name}')

    # расчитать время готовки всех продуктов в минутах
    def count_product_time(self):
        for product in self.ProductList:
            self.timeCreation += product.cooking_time
        return self.timeCreation

    # расчитать время доставки продуктов курьером
    def count_courier_time(self, facility_position: tuple = (0, 0), client_position: tuple = (0, 0), courier_speed = 5):
        #Расстояние через евклидову метрику
        distance = ((facility_position[0] - client_position[0]) ** 2) + ((facility_position[1] - client_position[1]) ** 2) ** 0.5
        return (distance / courier_speed * 60)

    