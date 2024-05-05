import threading
import time

def worker1():
    print('worker 1 started')
    time.sleep(2)
    print('worker 1 end')
    
def worker2():
    print('worker 2 started')
    time.sleep(3)
    print('worker 2 end')
    

t1=threading.Thread(target=worker1)
t2=threading.Thread(target=worker2)
t1.start()
t2.start()
print('outside thread blocks')