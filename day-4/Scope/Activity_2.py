# Use the nonlocal keyword in a nested function to maintain a counter in the outer function.

print("Value of counter using nonlocal is : ", end="")
 
def outer():
    counter = 5
 
    def inner():
        nonlocal counter
        counter += 1
    inner()
    print(counter)
 
outer()
print("Value of counter without using nonlocal is : ", end="")
def outer():
    counter = 5
 
    def inner():
        counter = 6
    inner()
    print(counter)

outer()