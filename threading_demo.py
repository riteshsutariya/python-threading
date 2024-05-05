import threading
import time

def func():
    print("thread task initiated")
    time.sleep(2)
    print("thread task end")

t=threading.Thread(target=func)
t.start()

print('outside thread block')