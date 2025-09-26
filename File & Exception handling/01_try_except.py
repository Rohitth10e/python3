menu = ["tea","coffee","chai"]

try:
    menu["lasagna"]
except:
    print("item not in menu")
finally:
    print("try ordering again")