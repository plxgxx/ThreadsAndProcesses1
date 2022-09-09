import datetime
import logging
import time
import threading
from multiprocessing import Process



def ticket_maker(start, end):
    print(f'args: {start}, {end}')
    for itm in range(start, end):
        a1 = f'{itm:06}'
        if int(a1[0]) + int(a1[1]) + int(a1[2]) == int(a1[3]) + int(a1[4]) + int(a1[5]):
            #print(f"The happy ticket is: {itm}") Щоб продивитись обрахунки
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

    procs = []
    proc1 = Process(target=ticket_maker(1, 200000))  # instantiating without any argument
    procs.append(proc1)
    proc1.start()

    # instantiating process with arguments
    proc2 = Process(target=ticket_maker(200000, 500000), args=(1,))
    procs.append(proc2)
    proc2.start()

    proc3 = Process(target=ticket_maker(500000, 700000))
    procs.append(proc3)
    proc3.start()

    proc4 = Process(target=ticket_maker(700000, 900000), args=(1,))
    procs.append(proc4)
    proc4.start()

    proc5 = Process(target=ticket_maker(900000, 999999), args=(1,))
    procs.append(proc5)
    proc5.start()

    # complete the processes
    for proc in procs:
        proc.join()

    end_time2 = time.perf_counter()
    print(f"MultiProcessing ended in {end_time2 - start_time2:0.4f} seconds")