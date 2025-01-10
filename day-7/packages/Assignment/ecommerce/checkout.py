from .cart import myCart
def total_cost():
    total = 0
    for item in myCart:
        price = item.get('item').get('price', 0)
        quantity = item.get('quantity', 0)
        total += price * quantity
    return total