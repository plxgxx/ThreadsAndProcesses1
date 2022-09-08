import datetime
import logging
import time
import threading
from multiprocessing import Process

def ticket_maker(start, end):
    for itm in range(start, end):
        a1 = f'{itm:06}'
        if int(a1[0]) + int(a1[1]) + int(a1[2]) == int(a1[3]) + int(a1[4]) + int(a1[5]):
            print(f"The happy ticket is: {itm}")
            with open("a1.txt", "a") as res:
                res.write(a1)

if __name__  == "__main__":

    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO,
                        datefmt="%H:%M:%S")
    start_time1 = time.perf_counter()
    logging.info("Main    : before creating thread")
    x = threading.Thread(target=ticket_maker(500000, 511155), args=(1,))
    logging.info("Main    : before running thread")
    x.start()
    logging.info("Main    : wait for the thread to finish")
    # x.join()
    logging.info("Main    : all done")

    end_time1 = time.perf_counter()
    print(f"Threading ended in {end_time1 - start_time1:0.4f} seconds")

    start_time2 = time.perf_counter()
    start = 1
    ending_point = 999999
    procs = []
    proc = Process(target=ticket_maker(500000, 510000))  # instantiating without any argument
    procs.append(proc)
    proc.start()

    # instantiating process with arguments
    for start in range(ending_point):
        proc = Process(target=ticket_maker(500000, 510000), args=(start,))
        procs.append(proc)
        proc.start()

    # complete the processes
    for proc in procs:
        proc.join()

    end_time2 = time.perf_counter()
    print(f"MultiProcessing ended in {end_time2 - start_time2:0.4f} seconds")