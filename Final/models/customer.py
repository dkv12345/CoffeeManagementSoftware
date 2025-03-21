class Customer:
    def __init__(self, customer_id, name, phone, customer_type):
        self.id = customer_id
        self.name = name
        self.phone = phone
        self.customer_type = customer_type
    def __str__(self):
        return f"{self.id}\t{self.name}\t{self.phone}\t{self.customer_type}"
