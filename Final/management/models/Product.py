class Product:
    def __init__(self,id,name,price,quantity):
        self.id=id
        self.name=name
        self.price=price
        self.quantity=quantity
    def __str__(self):
        return f"{self.id}\t{self.name}\t" \
               f"{self.price}\t{self.quantity}"