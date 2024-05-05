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
    
def worker3():
    print('worker 3 started')
    time.sleep(2)
    print('worker 3 end')
    

t1=threading.Thread(target=worker1)
t2=threading.Thread(target=worker2)
t3=threading.Thread(target=worker3)
t1.start()
t1.join()
t2.start()
t2.join()
# when controller comes here t3 will be started and controll will move to further line, and not wait until t3 terminates
t3.start()
print('outside thread blocks')