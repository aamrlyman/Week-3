
from grocery.shopping_cart import Shopping_Cart

class Customer: 

    def __init__(self, name):
        self.customer_name = name
        self.cart = Shopping_Cart()

    def append_product(self, product):
        self.cart.products_in_cart.append(product)
        print(f'{product.name} was added to your cart')
    
    def view_shopping_cart(self):
        current_shopping_cart = ''
        for products in self.cart.products_in_cart:
            current_shopping_cart += products.name + ", "
        if current_shopping_cart == '':
            print("Shopping cart is now empty")
        else: 
            print(current_shopping_cart)
