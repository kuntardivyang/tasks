# Create a package ecommerce with the following structure:
# 	ecommerce/
#      ├── __init__.py
#      ├── cart.py
#      ├── checkout.py
#  main.py
# cart.py: Add a function add_to_cart(prod, quantity).
# checkout.py: Calculate the total cost of items in the cart.
# Use these in a main script to simulate a basic shopping process.
from ecommerce import add_to_cart, total_cost, display_cart
import logging

logging.basicConfig(filename="errors.log", 
                    format='%(asctime)s %(message)s',
                    filemode='a+')

logger = logging.getLogger()

class Shopping:
    products = [{'name': 'Iphone', 'price': 100000}, 
            {'name': 'Samsung', 'price': 120000}, 
            {'name': 'Vivo', 'price': 20000}]
    
    def add(self):  
        flag = True
        while flag:
            for i in range(len(Shopping.products)):
                print(f'ID. {i + 1}, {Shopping.products[i]}')
                
            user_input = input('\n Enter Id of item You want to add in cart \n to stop adding type QUIT. \n')
            if user_input.strip().lower() == 'quit':
                flag = False
                continue
            
            quantity = int(input('Enter No. of quantity '))
            add_to_cart(Shopping.products[int(user_input) - 1], quantity)

    def calculate_total(self):
        print(f"Total cost of items in the cart: {total_cost()}")

obj = Shopping()
try :
    obj.add()
    obj.calculate_total()
    display_cart()
except Exception as e:
    logger.error(e)