from facility import Facility

class Cart:
    def __init__(self):
        self.facility = None
        self.list_products = []
        self.additional_dict = dict()
        
    def add_to_cart(self, product):
        self.list_products.append(product)
    
    def add_addition(self, product_name, additional):
        if product_name not in self.additional_dict:
            self.additional_dict[product_name] = []
        self.additional_dict[product_name].append(additional)
    
    def clear_cart(self):
        self.list_products = []
        self.additional_dict = {}
    
    def pop_product(self, product_name):
        new_products = []
        for prod in self.list_products:
            if prod.name != product_name:
                new_products.append(prod)
        self.list_products = new_products
        self.additional_dict.pop(product_name)
        
    def confirm_cart(self):
        return self
