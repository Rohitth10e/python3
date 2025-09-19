from multiprocessing import Process
import time

def cpu_heavy():
    print(f"Crunching some numbers....")
    total = 0
    for i in range(10**8):
        total += i
    print(f"Done with {total} numbers...")

if __name__ == '__main__':
    start = time.time()

    processes = [Process(target=cpu_heavy()) for _ in range(2)]
    [t.start() for t in processes]
    [t.join() for t in processes]

    print(f"total-time: {time.time() - start:.2f} seconds")
