from functools import wraps

def log_activity(func):
    @wraps(func)
    def wrappper(*args, **kwargs):
        print(f"calling: {func.__name__}")
        result = func(*args, **kwargs)
        print(f"finished: {func.__name__}")
        return result
    return wrappper

@log_activity
def brew_chai(type, milk="no"):
    print(f"Brewing {type} chai & milk {milk}")

brew_chai("Masala","yes")