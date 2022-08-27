class Shopping_Cart:
    def __init__(self):

        self.products_in_cart = []

    def get_cart_cost(self):
        total_cost = 0
        for products in self.products_in_cart:
            total_cost += products.price
        return f'Shopping cart total is: ${total_cost}'
    
    def append_product(self, product):
        self.products_in_cart.append(product)
        print(f'{product.name} was added to your cart')
    
    def empty_shopping_cart(self):
        self.products_in_cart.clear()
        print('Shopping cart is now empty')

    def view_shopping_cart(self):
        current_shopping_cart = ''
        for products in self.products_in_cart:
            current_shopping_cart += products.name + ", "
        if current_shopping_cart == '':
            print("Shopping cart is now empty")
        else: 
            print(current_shopping_cart)
        
