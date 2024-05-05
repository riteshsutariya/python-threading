import time
import threading
import logging
import psutil

def print_cpu_usage():
    while True:
        cpu_usage=psutil.cpu_percent(interval=1)
        print(f'CPU Usage: {cpu_usage}%')
        time.sleep(4)

def print_memory_usage():
    while True:
        memory_usage=psutil.virtual_memory().percent
        print(f'Memory Usage: {memory_usage}%')
        time.sleep(4)

t1=threading.Thread(target=print_cpu_usage)
t2=threading.Thread(target=print_memory_usage)

t1.start()
t2.start()