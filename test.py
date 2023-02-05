import concurrent.futures
import signal
import os
import sys
import multiprocessing as mp
import time

def run_process():
    print(f"Child process: {os.getpid()}")
    def handler(signum, frame):
        print(f'Signal handler called with signal {signum} for process:{os.getpid()}\n')

    signal.signal(signal.SIGTERM, handler)
    time.sleep(2000000)

def handler(signum, frame):
    print(f'Signal handler called with signal {signum} for process :{os.getpid()}\n')
    print(frame)

signal.signal(signal.SIGTERM, handler)

if __name__ == '__main__':

    with concurrent.futures.ProcessPoolExecutor(max_workers=2, mp_context=mp.get_context("spawn")) as executor:

        print(f"main process: {os.getpid()}")
        for i in range(2):
            executor.submit(run_process)
        print(f"all process submitted")










