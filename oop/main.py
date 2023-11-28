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

    def instantiate_from_csv(self,):
        
    # Function to represent this item
    def __repr__(self):
        return f"Item('{self.name}','{self.price}','{self.quantity}')"

item1 = Item("Phone",100,5)
item2 = Item("Laptop",1000,3)
item3 = Item("Cable",10,5)
item4 = Item("Mouse",50,5)
item5 = Item("Keyboard",75,5)

print(Item.all)