class Chai:
    temperature = "hot"
    strength = "Strong"

# Chai cutting = new Chai #object creation
cutting = Chai()
print(cutting.temperature)
cutting.temperature = "cool"
cutting.type = "large"
print("after changing: ",cutting.temperature)
print(Chai.temperature)

del cutting.temperature
del cutting.strength
print("cutting",cutting.temperature)
print("cutting",cutting.type)