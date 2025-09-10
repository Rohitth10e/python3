# concurrency: multiple tasks making progress together
# parallelism: multiple tasks are working simultaneously with different cores

# concurrency --> 1. threading.Thread 2. asyncio
# parallelism --> 1. multiprocessing.Process 2. concurrent.futures.ProcessPoolExecuter

import threading
import time

def take_orders():
    for i in range(1,4):
        print("order #",i)
        time.sleep(2)

def brew_coffee():
    for i in range(1,4):
        print("coffee #",i)
        time.sleep(3)

# create threads

order_thread = threading.Thread(target=take_orders)
brew_thread = threading.Thread(target=brew_coffee)

order_thread.start()
brew_thread.start()

# wait for both to finish

order_thread.join()
brew_thread.join()

print("Order taken and coffee brewed")

# it seems like they're working independently but they're working synchronously
