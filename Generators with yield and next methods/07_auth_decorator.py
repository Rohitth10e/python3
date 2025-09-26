from functools import wraps

def require_admin(func):
    @wraps(func)
    def wrapper(user_role):
        if user_role != "admin":
            print("access denied: admin only")
        else:
            return func(user_role)
    return wrapper

@require_admin
def access_tea_inventory(user_role):
    print(f"access to tea inventory {user_role} granted")

access_tea_inventory("admin")
access_tea_inventory("user")