class BaseChai:
    def __init__(self, type_):
        self.type = type_
    def prepare(self):
        print(f"Preparing {self.type} chai....")


class MasalaChai(BaseChai):
    def add_spices(self):
        print("Adding cardamom, ginger, cloves")

class ChaiShop:
    # composition
    chai_cls = BaseChai

    def __init__(self):
        self.chai = self.chai_cls("Regular")

    def serve(self):
        self.chai.prepare()
        print(f"Serving {self.chai.type} chai....")

class FancyChaiShop(ChaiShop):
    chai_cls = MasalaChai

    def serve(self):
        self.chai.type = "Masala"
        self.chai.prepare()
        self.chai.add_spices()

chai = FancyChaiShop()
chai.serve()
chai.chai.add_spices()