from functools import wraps

def my_dec(func):
    @wraps(func)
    def wrapper():
        print("Before function runs")
        func()
        print("After function runs")
    return wrapper

@my_dec
def greet():
    print("Hello from decorator")
