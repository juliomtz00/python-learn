class Item:
    # The function init will be used whenever the class or object is called
    # Variable types can be added to the inputs to make them more robus
    # If a default value is set as in quantity, the type is automatically set.
    def __init__(self, name: str,price: float,quantity=0):
        # assert statements are a used keyword that is used to check if there's a match with what is expected
        # Run validations to the recieved arguments
        assert price >= 0, f"Price {price} must be greater than zero!"
        assert quantity >= 0, f"Quantity {quantity} must be greater than zero!"

        # Assign to self object
        self.name = name
        self.price = price
        self.quantity = quantity

    def calculate_total_prince(self):
        return self.price * self.quantity

item1 = Item("Phone",100,5)
item2 = Item("Laptop",1000,3)

print(item1.calculate_total_prince())
print(item2.calculate_total_prince())

