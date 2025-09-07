class Chai:
    origin = "India"

print(Chai.origin)

Chai.is_hot = True

# creating objects from class Chai

masala = Chai()
print(f"Masala: {masala.origin}")
print(f"Masala: {masala.is_hot}")
masala.is_hot = False
print(f"Masala: {masala.is_hot}")
masala.flavor = "barbeque"
print(f"Masala: {masala.flavor}")
