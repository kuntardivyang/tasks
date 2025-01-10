myCart = []
def add_to_cart(item, quantity):
    myCart.append({'item' : item, 'quantity' : quantity })
    print(f"Added {quantity} : {item} to the cart.")

def display_cart():
    for i in myCart:
        print(i)