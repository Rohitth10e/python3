class Chai:
    # creating a constructor by __init__
    # - it runs automatically when you create a new object like cutting = Chai().
    def __init__(self,type_,size):
        self.type = type_
        self.size = size

    def summary(self):
        return f"{self.size} ml of {self.type}"

chai_order = Chai('cutting','100ml')
print(chai_order.summary())