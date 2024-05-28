from payment import Payment
from cart import Cart
from courier import Courier, Couriers
from order import Order
from facility import Facility, Facilities
from product import Product
from Review_and_Stock import Review, Reviews

Clients = []
    

class Client:
    def __init__(self, name="Noname", phone_number=0, \
                 cart=Cart(), bonus=0):
        self.name = name
        self.phone_number = phone_number
        self.cart = cart
        self.bonus = bonus
        self.payment = Payment()
        Clients.append(self)
    
    def choose_facility(self):
        print('Выберете ресторан: ')
        for facility in Facilities:
            print(facility.name)
        self.cart = Cart()
        name_of_facility = input()
        for facility in Facilities:
            if facility.name == name_of_facility:
                self.cart.facility = facility
                self.choose_product()
                return
        print('Ресторана с таким названием не существует')
        
    def choose_product(self):
        if self.cart.facility == None:
            print('Сначала выберете ресторан')
            return
        print('Добавьте продукт в корзину')
        for product in self.cart.facility.menu:
            print(product.name)
        name_of_product = input()
        for product in self.cart.facility.menu:
            if product.name == name_of_product:
                cart_product = product
                self.cart.add_to_cart(cart_product)
                for addition in product.additional:
                    print(addition[0], addition[1])
                print('Нужны ли дополнения к продукту? (y / n)')
                verdict = input()
                if verdict == 'n':
                    return 
                print('Солько нужно дополнений?')
                cnt = int(input())
                for i in range(cnt):
                    self.add_additional(cart_product)
                return
        print('Такого продукта не существует')
    
    def add_additional(self, product):
        while True:
            print('Выберете дополнение к основному продукту')
            for addition in product.additional:
                print(addition[0], addition[1])
            additional_product = input()
            for addition in product.additional:
                if addition[0] == additional_product:
                    self.cart.add_addition(product.name, addition)
                    print('Дополнение добавлено в корзину')
                    return 
            print('Такого дополнения к этому продукту не существует')
    
    def confirm_order(self):
        order = Order()
        print('Введите адрес, куда привезти негров(зачеркнуто) заказ')
        order.address = input()
        for product in self.cart.list_products:
            order.ProductList.append(product)
        for additional_key in self.cart.additional_dict:
            # print(additional)
            for addition in self.cart.additional_dict[additional_key]:
                add_product = Product()
                add_product.name = addition[0]
                add_product.price = addition[1]
                order.ProductList.append(add_product)
        # print([(elem.name, elem.price) for elem in order.ProductList])
        self.cart.facility.add_order(order)
        self.call_delivery_boy()
        self.get_payment()
        
    def get_payment(self):
        cost = 0
        if self.cart.facility == None:
            print('Сначала выберете ресторан')
            return 
        print('Ресторан:', self.cart.facility.name)
        print('Название | Цена')
        for product in self.cart.list_products:
            print(product.name, '|', product.price)
            cost += product.price
        if self.cart.additional_dict:
            print('Допы: ')
            print(self.cart.additional_dict.keys())
            for product_name in self.cart.additional_dict.keys():
                print('Название | Цена')
                for dop in self.cart.additional_dict[product_name]:
                    print(dop[0], dop[1])
                    cost += dop[1]
        print('Счет:', cost)
        self.payment.make_payment()
        self.cart = Cart()
        
    def call_delivery_boy(self):
        self.cart.facility.give_order(Couriers)
    
    def cancel_order(self):
        print('Вы отменили заказ. Корзина пуста.')
        self.cart.clear_cart()
        
    def make_rate(self):
        review = Review()
        print('Опишите ваше мнение о заказе')
        review.text = input()
        print('Дайте оценку заказа от 1 до 10')
        review.rate = int(input())
        print('Опишите плюсы заказа')
        review.plus = input()
        print('Опишите минусы заказа')
        review.minus = input()
        Reviews.append(review)
    
    def __str__(self):
        return "name: {}, phone_number: {}, bonus: {}".format( \
            self.name, self.phone_number, self.bonus)

def add_client(name="Noname", phone_number=0, \
                 cart=Cart(), bonus=0):
    Clients.append(Client(name=name, 
                   phone_number=phone_number, cart=Cart(), bonus=bonus))
add_client('Olegator')