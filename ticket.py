import time
import threading
from multiprocessing import Process



def ticket_maker(start, end, file_name):
    print(f'args: {start}, {end}')
    a2 = 0
    for itm in range(start, end):
        a1 = f'{itm:06}'
        if int(a1[0]) + int(a1[1]) + int(a1[2]) == int(a1[3]) + int(a1[4]) + int(a1[5]):
            a2 += 1
    print(f'exit {file_name} {a2}')

if __name__  == "__main__":


    print("Started the process of threading")
    start_time1 = time.perf_counter()

    threads = []

    x1 = threading.Thread(target=ticket_maker, args=(1, 200000, 'thread1'))
    threads.append(x1)

    x2 = threading.Thread(target=ticket_maker, args=(200000, 500000, 'thread2'))
    threads.append(x2)

    x3 = threading.Thread(target=ticket_maker, args=(500000, 700000, 'thread3'))
    threads.append(x3)

    x4 = threading.Thread(target=ticket_maker, args=(700000, 900000, 'thread4'))
    threads.append(x4)

    x5 = threading.Thread(target=ticket_maker, args=(900000, 999999, 'thread5'))
    threads.append(x5)

    x1.start()
    x2.start()
    x3.start()
    x4.start()
    x5.start()

    for x in threads:
        x.join()

    end_time1 = time.perf_counter()
    print(f"Threading ended in {end_time1 - start_time1:0.4f} seconds")

    print("Started the process of multiprocessing")
    start_time2 = time.perf_counter()

    procs = []
    proc1 = Process(target=ticket_maker, args=(1, 200000, 'process1'))  # instantiating without any argument
    procs.append(proc1)

    # instantiating process with arguments
    proc2 = Process(target=ticket_maker, args=(200000, 500000, 'process2'))
    procs.append(proc2)

    proc3 = Process(target=ticket_maker, args=(500000, 700000, 'process3'))
    procs.append(proc3)

    proc4 = Process(target=ticket_maker, args=(700000, 900000, 'process4'))
    procs.append(proc4)

    proc5 = Process(target=ticket_maker, args=(900000, 999999, 'process5'))
    procs.append(proc5)

    proc1.start()
    proc2.start()
    proc3.start()
    proc4.start()
    proc5.start()

    # complete the processes
    for proc in procs:
        proc.join()

    end_time2 = time.perf_counter()
    print(f"MultiProcessing ended in {end_time2 - start_time2:0.4f} seconds")
    print(f"Threading ended in {end_time1 - start_time1:0.4f} seconds")