from item import Item

class Phone(Item):
     def __init__(self, name: str,price: float,quantity=0,broken_phones=0):
        # assert statements are a used keyword that is used to check if there's a match with what is expected
        # Run validations to the recieved arguments
        assert price >= 0 and price <= 2000, f"Price {price} must be greater than zero and lower than 2000!"
        assert broken_phones >= 0, f"Broken phones {broken_phones} must be greater than zero!"

        # Assign to self object
        self.name = name
        self.price = price
        self.quantity = quantity
        self.broken_phones = broken_phones

        # Actions to execute
        Phone.all.append(self)