from cell_phone import Cell_Phone

Ricks_Cell = Cell_Phone('iphone 8', 801-413-6276, 'Rick')
John_cell = Cell_Phone('galaxy9', 8013245532, 'John')

Ricks_Cell.send_text_message(John_cell)
print(John_cell.messages)

from itertools import product
from alarm_clock import Alarm_Clock
from customer import Customer
from product import Product
from shopping_cart import Shopping_Cart

# alarm_clock_1 = Alarm_Clock('4:50 PM', '6:00 AM')

# print(alarm_clock_1.current_time)

# alarm_clock_1.set_clock_time()

# alarm_clock_1.turn_alarm_on_off()

customer_1 = Customer("Rick")

apple_juice = Product("Apple juice", 4, "food")
grape_juice = Product("Orange juice", 4, "food")
orange_juice = Product("Orange juice", 4, "food")

customer_1.cart.append_product(orange_juice)
customer_1.cart.append_product(grape_juice)
customer_1.cart.append_product(apple_juice)

customer_1.cart.view_shopping_cart()
print(customer_1.customer_name)

total_order = customer_1.cart.get_cart_cost()
print(total_order)

customer_1.cart.empty_shopping_cart()

customer_1.cart.view_shopping_cart()