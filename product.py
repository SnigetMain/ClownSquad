class Product:
    productId: str
    name: str
    costPrice: float

    def __init__ (self, productId: str, name: str, costPrice: float):
        self.productId = productId
        self.name = name
        self.costPrice = float(costPrice)
    def __hash__(self):
        return hash(self.name)
    pass