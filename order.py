from dataclasses import dataclass
from enum import Enum
from product import Product
# from typing import List
from client import Client
from facility import Facility
import uuid

class Status(Enum):
    PROCESSING = 0 #обработка
    ACCEPTED = 1  # приянт
    INSTOCK = 2 #приготовление
    ONTHEWAY = 3 #в пути
    INPOINT = 4 # в пунткте
    RECEIVED = 5 #получен
    CANCEL = 6 #отменен

@dataclass
class Order:
    orderId: str
    status: Status
    ProductList: list[Product]
    timeCreation: tuple[int]
    address: str
    client: Client
    facility: Facility
    #collector: User
    

    def __init__(self,  client:Client,facilty:Facility,status: Status=Status.PROCESSING, ProductList: list[Product]=[], adress="", timeCreation = (0,0)):
        self.orderId = uuid.uuid1()
        self.client = client
        self.status = status
        self.facility = facilty
        self.ProductList = ProductList
        self.timeCreation = timeCreation
        self.address = adress
        #self.collector = collector

    def ChangeStatus(self,status:Status):
        self.status = status

    def printOrder(self):
        print(f'ID: {self.orderId}')
        print(f'Кому: {self.client.name}')
        print(f'Статус заказа: {self.status.name}')