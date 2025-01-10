# Build a program that:
#   Creates a Product class with attributes name, price, and stock.
#   Adds methods to sell a product, restock, and display details.
#   Implements error handling to ensure valid input for price (must be positive) and stock (must be an integer).
#   Uses a lambda function to apply a discount to all product prices.
#   Writes product details into a file and reads them back, sorting the products by stock quantity.


class Product:
    id = 0
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock
        Product.id += 1
        self.id = Product.id
        
    def sell_stock(self, quantity):
        self.stock -= quantity
        
    def restock(self,quantity):
        self.stock += quantity
        
    def display_details(self):
        print(f'Product\'s ID {self.id}')
        print(f'Product\'s name {self.name}')
        print(f'Product\'s price {self.price}')
        print(f'Product\'s stock {self.stock}')

products=[]

class Project:
    
    def add_product():      
        flag = True
        while flag:
            '''
            loop to add products

            '''
            user_input = input('''
                               Type Product's name,price and stock separated by space like ( 'Soap' 20 100 ) \n
                               to quit product adding just type \'quit\'
                               ''')

            if user_input.lower()=='quit' : 
                flag = False
            else :
                user_input = user_input.strip().split()
                try:
                    name = user_input[0]
                    price = float(user_input[1])
                    if price < 0:
                        print('Price of Product must be positive. ')
                        continue
                except ValueError:
                    print('Price must be in Numberic type')
                    continue
                try : 
                    stock = int(user_input[2])
                except ValueError:
                    print('Stock must be in integer type. ')
                    continue
                products.append(Product(name,price,stock))
                print('Product Added Succefully')
    
    def discount_products(): 
        # Applying discount to all products
        apply_discount = lambda price, discount : price - (price*discount)/100
        discount = int(input('Enter discount percentage you want to apply on products : '))
        for i in range(len(products)):
            product = products[i]
            product.price = apply_discount(product.price, discount)
            products[i] = product
    
    def writing(): 
        # Writing All products to products.txt
        file = open('products.txt','w')
        products.sort(key = lambda product: product.stock)
        for i in range(len(products)):
            file.write(f'Product ID . {products[i].id} \n')
            file.write(f'Product\'s name {products[i].name} \n')
            file.write(f'Product\'s price {products[i].price} \n')
            file.write(f'Product\'s stock {products[i].stock} \n\n')
    
    def sell_stock():
        pro_id=int(input('enter id of product whose stock you want to sell : ')) - 1
        quantity = int(input('Enter Sell Quantity of Stock '))
        product = products[pro_id]
        product.sell_stock(quantity)
        products[pro_id] = product
    
    def re_stock():
        pro_id=int(input('enter id of product whose stock you want to add : ')) - 1
        quantity = int(input('Enter Quantity of Stock '))
        product = products[pro_id]
        product.restock(quantity)
        products[pro_id] = product
        
Project.add_product()
Project.discount_products()
Project.writing()
print()
product1=products[0]
product1.display_details()
print()
Project.sell_stock()
product1.display_details()
print()
Project.re_stock()
product1.display_details()
