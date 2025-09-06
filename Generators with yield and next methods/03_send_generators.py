def chai_customer():
    print("welcome! what would you like to do?")
    order = yield
    while True:
        print(f"Preparing: {order}")
        order = yield #if u get rid of this line, this will run infinite loop
stall = chai_customer()
next(stall) #start the generator

stall.send("masala chai")
stall.send("lemon chai")