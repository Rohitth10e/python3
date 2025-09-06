def local_chai():
    yield "Masala chai"
    yield "Ginger chai"

def imported_chai():
    yield "Matcha"
    yield "Oolong"

def full_menu():
    yield from local_chai()
    yield from imported_chai()

menu = full_menu()
print(next(menu))