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
            print(f"The happy ticket is: {itm}") #Щоб продивитись обрахунки
            with open("a1.txt", "a") as res:
                res.write(a1)

if __name__  == "__main__":


    print("Started the process of threading")
    start_time1 = time.perf_counter()

    x1 = threading.Thread(target=ticket_maker(1, 200000), args=(1,))
    x1.start()

    x2 = threading.Thread(target=ticket_maker(200000, 500000), args=(1,))
    x2.start()

    x3 = threading.Thread(target=ticket_maker(500000, 700000), args=(1,))
    x3.start()

    x4 = threading.Thread(target=ticket_maker(700000, 900000), args=(1,))
    x4.start()

    x5 = threading.Thread(target=ticket_maker(900000, 999999), args=(1,))
    x5.start()

    end_time1 = time.perf_counter()
    print(f"Threading ended in {end_time1 - start_time1:0.4f} seconds")

    print("Started the process of multiprocessing")
    start_time2 = time.perf_counter()

    procs = []
    proc1 = Process(target=ticket_maker(1, 200000), args=(1,))  # instantiating without any argument
    procs.append(proc1)
    proc1.start()

    # instantiating process with arguments
    proc2 = Process(target=ticket_maker(200000, 500000), args=(1,))
    procs.append(proc2)
    proc2.start()

    proc3 = Process(target=ticket_maker(500000, 700000), args=(1,))
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