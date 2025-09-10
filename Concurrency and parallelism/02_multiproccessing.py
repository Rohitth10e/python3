# parallelism -> multiprocessing
from multiprocessing import Process
import time

def brew_chai(name):
    print(f"start of brewing {name} chai")
    time.sleep(3)
    print(f"end of brewing {name} chai")

if __name__ == "__main__":
    chai_makers = [
        Process(target=brew_chai, args=(f"Chai maker #{ i+1 }",))
        for i in range(3)
    ]

    # start all process
    for p in chai_makers:
        p.start()

    # wait for all to complete
    for p in chai_makers:
        p.join()

    print("all done")