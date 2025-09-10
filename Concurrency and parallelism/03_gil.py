# python provides a way to deal with race condition i.e via concept to GLI

'''
Suppose there are 2 threads and thread 1 wants to change the value from 4 to 5 and thread 2 from 4 to 6
to solve this issue python has something called as 'mutex', i.e who ever has the mutex can edit the value and no other guy can go ahead and edit the value in the memeory i.e a guy with mutex has full control, once the job is done the mutex is passed onto other guy/thread. this effectively solves race-condtion
'''

import threading
import time

def brew_chai():
    print(f"{threading.current_thread().name} started brewing...")
    count = 0
    for _ in range(100_00_000):
        count += 1
    print(f"{threading.current_thread().name} finished brewing...")

thread_1=threading.Thread(target=brew_chai, name="barista-1")
thread_2=threading.Thread(target=brew_chai, name="barista-2")

start = time.time()
thread_1.start()
thread_2.start()
thread_1.join()
thread_2.join()
end = time.time()

print(f"total time: , {end-start:.2f} secs")