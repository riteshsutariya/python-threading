import threading
import time


def server_status():
    while True:
        print('[Server Status]: Running')
        time.sleep(2)
        
t=threading.Thread(target=server_status)

# setting t as daemon thread
# note: you must have to set daemon before start()
t.daemon=True

t.start()

def run_server():
    for _ in range(10):
        print('[Server]: Processing Data...')
        time.sleep(1)
        
run_server()
# t thread will come to end once main thread completes it work
''' 
reason: daemon threads are background threads that automatically exit as soon as all non-daemon threads
        have completed(typically the main program)
'''
print('Server Shutdown!')