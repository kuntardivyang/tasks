#Tuples
# Use tuple unpacking to swap values of two variables.


    

def activity_3():
    tuple_one = ('Car', 'Truck', 'Jeep', 'Bike', 'Scooter')
    one, two, *three = tuple_one
    tuple_one = (two, one, *three) #swapping car and truck
    print(tuple_one)

activity_3()