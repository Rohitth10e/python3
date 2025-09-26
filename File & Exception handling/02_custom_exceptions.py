def chai(flavor):
    if flavor not in ["ginger", "elaichi", "honey"]:
        raise ValueError("Flavor must be one of ['ginger', 'elaichi', 'honey']")
    print("Chai flavor is " + flavor)

chai("ginger")

class OutOfStockException(Exception):
    pass

def prepare_chai(milk=0):
    if milk == 0:
        raise OutOfStockException("Milk out of stock")
    print("preparing chai")

prepare_chai()