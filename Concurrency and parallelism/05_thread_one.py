import threading
import time

def boil_milk():
    print(f"Boiling Milk")
    time.sleep(2)
    print(f"Milk boiled")

def toast_bun():
    print(f"Toasting Bun")
    time.sleep(3)
    print(f"Done toasting Bun")

start = time.time()

thread_01 = threading.Thread(target=boil_milk)
thread_02 = threading.Thread(target=toast_bun)

thread_01.start()
thread_02.start()

thread_01.join()
thread_02.join()

print(f"Total time: {time.time()-start:.2f}")