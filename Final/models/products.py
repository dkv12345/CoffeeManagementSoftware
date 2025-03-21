class Product:
    def __init__(self, id, name, price, quantity):
        self.id = id
        self.name = name
        self.price = price
        self.quantity = quantity

    def to_dict(self):  # Chuyển đối tượng thành dictionary
        return {
            "id": self.id,
            "name": self.name.strip(),  # Loại bỏ khoảng trắng thừa nếu có
            "price": self.price,
            "quantity": self.quantity
        }

    def __str__(self):
        return f"Product(ID: {self.id}, Name: {self.name.strip()}, Price: {self.price}, Quantity: {self.quantity})"
