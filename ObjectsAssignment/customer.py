from math import prod
from shopping_cart import Shopping_Cart

class Customer: 

    def __init__(self, name):
        self.customer_name = name
        self.cart = Shopping_Cart()

    
