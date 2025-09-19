import threading
import time

def cpu_heavy():
    print(f"Crunching some numbers....")
    total = 0
    for i in range(10**8):
        total += i
    print(f"Done with {total} numbers...")

start = time.time()

threads = [threading.Thread(target=cpu_heavy()) for _ in range(2)]
[t.start() for t in threads]
[t.join() for t in threads]

print(f"total-time: {time.time() - start:.2f} seconds")
