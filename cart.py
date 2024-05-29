from facility import Facility

#класс корзина
class Cart:
    is_confirmed: bool = False #подтверждена ли корзина
    order_amount: float = 0 #сумма заказа корзины

    def __init__(self): 
        self.facility = None
        self.list_products = [] #название продукта и его кол-во
        self.additional_dict = dict()

    def add_to_cart(self, product): #добавить в корзину
        self.list_products.append([product, 1])

    def add_addition(self, product, additional): #дополнение к продукту
        if product.name not in self.additional_dict:
            self.additional_dict[product.name] = []
        self.additional_dict[product.name].append(additional)

    def set_product_count(self, product, count_product): #установить кол-во продуктов
        if count_product >= 0:
            for i in range(len(self.list_products)):
                if self.list_products[i][0] == product:
                    self.list_products[i][1] = count_product

    def clear_cart(self): #очистить корзину
        self.list_products = []
        self.additional_dict = {}

    def pop_product(self, product_name): #удалить продукт из корзины
        for i in range(len(self.list_products)):
            if self.list_products[i] == product_name:
                self.list_products.pop(i)
                break
        self.additional_dict.pop(product_name)

    def count_cost_cart(self): #подсчитать стоимость корзины
        for i in range(len(self.list_products)):
            self.order_amount += self.list_products[i][0].price * self.list_products[i][1]
            return self.order_amount

    def confirm_cart(self): #подтвердить
        self.is_confirmed = True

