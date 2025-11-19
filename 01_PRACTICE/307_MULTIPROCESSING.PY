from multiprocessing import Process
import os, time

def show_info():
    print(f"Process ID: {os.getpid()}")

if __name__ == "__main__":
    processes = []

    for _ in range(5):
        p = Process(target=show_info)
        p.start()
        processes.append(p)

    for p in processes:
        p.join()
