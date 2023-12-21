import csv

class Item:
    # The function init will be used whenever the class or object is called
    # Variable types can be added to the inputs to make them more robus
    # If a default value is set as in quantity, the type is automatically set.

    pay_rate = 0.8
    all = []

    def __init__(self, name: str,price: float,quantity=0):
        # assert statements are a used keyword that is used to check if there's a match with what is expected
        # Run validations to the recieved arguments
        assert price >= 0 and price <= 2000, f"Price {price} must be greater than zero and lower than 2000!"
        assert quantity >= 0, f"Quantity {quantity} must be greater than zero!"

        # Assign to self object
        self.name = name
        self.price = price
        self.quantity = quantity

        # Actions to execute
        Item.all.append(self)

    def calculate_total_prince(self):
        return self.price * self.quantity
    
    def apply_discount(self):
        self.price = self.price * Item.pay_rate

    @classmethod
    def instance_from_csv(cls):
        with open('items.csv','r') as f:
            reader = csv.DictReader(f)
            items = list(reader)

        for item in items:
            Item(
                name = item.get('name'),
                price = float(item.get('price')),
                quantity = int(item.get('quantity')),
            )

    @staticmethod
    def is_integer(num):
        # We will count out the floats that are point 0
        # For i.e: 5.0, 10.0
        if isinstance(num,float):
            # Count out the floats that are point 0
            return num.is_integer()
        elif isinstance(num,int):
            return True
        else:
            return False
        

    # Function to represent this item
    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}','{self.price}','{self.quantity}')"