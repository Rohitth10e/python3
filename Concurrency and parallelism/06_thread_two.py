import threading
import time

def prepare_chai(type_,wait_time):
    print(f'{type_} chai brewing')
    time.sleep(wait_time)
    print(f'{type_} chai brewed')

thread_1 = threading.Thread(target=prepare_chai, args=('masala',2))
thread_2 = threading.Thread(target=prepare_chai, args=('ginger',3))

thread_1.start()
thread_2.start()

thread_1.join()
thread_2.join()