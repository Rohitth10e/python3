class ChaiOrder:
    def __init__(self, tea_type, sweetness, size):
        self.tea_type = tea_type
        self.sweetness = sweetness
        self.size = size

    @classmethod
    def from_dict(cls, order_data):
        return cls(
            order_data["tea_type"],
            order_data["sweetness"],
            order_data["size"]
        )

    @classmethod
    def from_string(cls, order_str):
        tea_type, sweetness, size = order_str.split("-")
        return cls(tea_type, sweetness, size)


order1 = ChaiOrder.from_dict({"tea_type":"masala","sweetness":"little","size":"medium"})
print(order1.__dict__)
order2 = ChaiOrder.from_string("Ginger-Low-Small")
print(order2.__dict__)