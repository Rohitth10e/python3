#generators are always gonna come up with yield as keyword

'''
    1.You save memory
    2.You don't want the results immedietely
    3.lazy evaluation
'''

def serve_chai():
    yield 'cup 1: masala chai'
    yield 'cup 2: ginger chai'
    yield 'cup 3: elaichi chai'

stall = serve_chai()

for cup in stall:
    print(cup)

# the diff is in memory: the stall var is keeping a reference of whole func, the moment you run the loop it makes use of the value

# let's see diff bw regular and generator

def get_chai_list():
    return ["cup 1","cup 2","cup 3"]

def get_chai_gen():
    yield "cup 1"
    yield "cup 2"
    yield "cup 3"

chai = get_chai_gen()
#next you get the first value that you yield, then it's paused and keeps track in memory and if you go ahead and print it again, it gives you next val i.e cup 2 and when done yielding values it throws 'StopIteration' error
print(next(chai))
print(next(chai))
print(next(chai))
try:
    print(next(chai))
except StopIteration:
    print("StopIteration")