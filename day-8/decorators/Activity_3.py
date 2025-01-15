def cache(func):
    cache_data = None
    cached = False

    def wrapper():
        nonlocal cached, cache_data
        if cached:
            return cache_data
        result = func()
        cache_data = result
        cached = True
        return result

    return wrapper

def decorator(func):
    def uppercase():
        word = func()
        return word.upper()
    return uppercase

@cache
@decorator
def uppercasing():
    return input('Enter Your Word to make it uppercase: ')

print(uppercasing())
print(uppercasing())