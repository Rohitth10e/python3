class Chai:
    size = 150

    def describe(self):
        return f"Chai is: {self.size} ml"

cup = Chai()
print(cup.describe())
cup_two = Chai()
cup_two.size = 250
print(cup_two.describe())
# passing context to class
print(Chai.describe(cup_two))