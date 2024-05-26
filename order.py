from dataclasses import dataclass
from enum import Enum
from product import Product
# from typing import List
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
    timeCreation: str
    address: str
    #collector: User
    

    def __init__(self,  status: Status=0, ProductList: list[Product]=[], adress="", timeCreation = 0):
        self.orderId = uuid.uuid1()
        self.status = status
        self.ProductList = ProductList
        self.timeCreation = timeCreation
        self.address = adress
        #self.collector = collector

    def ChangeStatus(self,status:Status):
        self.status = status
