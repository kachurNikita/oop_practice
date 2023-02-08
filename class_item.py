
# Item class
class Item:
    # Class variable, will be the same for every instance
    discount = 0.5
    items_storage = []

    def __init__(self, name: str, price: float, quantity=0):
        # assert statements, to make check
        assert len(name) >= 1, f'Item name can not be an empty string'
        assert price >= 0, f'price {price}, can not be less then zero'
        assert quantity >= 0, 'Minimum item quantity is 0'
        # initialize instance attributes
        self.name = name
        self.price = price
        self.quantity = quantity

        # add new created item to list
        Item.items_storage.append(self)

    # Calculate total item quantity
    def calculate_price(self):
        return self.price * self.quantity

    # change state of item price using discount, but discount will be the same for each item
    def apply_discount(self):
        self.price = self.price * Item.discount

    # instance representation in human understanding way\
    def __repr__(self):
        return f'Item({self.name}, {self.price}, {self.quantity})'

    @classmethod
    def show_all_items(cls):
        for instance in Item.items_storage:
            return instance








# Specify wich data need to be  pass in