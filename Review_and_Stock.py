from payment import Payment
from cart import Cart
from courier import Courier, Couriers
from order import Order
from facility import Facility, Facilities
from product import Product

Reviews = []

class Review:
    user_name:str
    text:str
    rate:int
    plus:str
    minus:str
    comments:list[(str, str)]

    def __init__(self, user_name, text, rate, plus, minus):
        self.user_name = user_name
        self.text = text
        self.rate = rate
        self.plus = plus
        self.minus = minus
        self.comments = list()
    
    def print_review(self):
        print(self.user_name)
        print(f'Рейтинг: {self.rate * '★'}{(5 - self.rate) * '☆'}')
        print('Плюсы товара: ')
        print(self.plus)
        print('Минусы товара: ')
        print(self.minus)
        print('Комеентарии: ')
        print(self.text)
        self.comments_output()

    def comments_output(self):
        index = 0
        while index != len(self.comments) and index >= 0:
            print(self.comments[index][0], '\n', self.comments[index][0])
            n = input('Введите 1, если хотите перейти к предыдущему, 2 - если к следующему, 3 - если хотите закрыть')
            if n == 1:
                index -= 1
            elif n == 2:
                index += 1
            else:
                break

class Stock:
    facility:Facility
    product:Product
    discount:int
    description:str
    
    def __init__(self, facility,product, discount, description, condition):
        self.product = product
        self.discount = discount
        self.description = description
        self.condition = condition
        self.facility = facility

    def stock_using(self, cart):
        if(self.condition(cart)):
            return self.discount
        else:
            #print('Условия не соблюдены!')
            return 0