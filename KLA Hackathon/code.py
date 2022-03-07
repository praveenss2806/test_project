#hello my name is praveen
#hello my name is yashodhar
import threading
import time

start=time.perf_counter()

def do_something():
    print('Sleeping 1 Second')
    time.sleep(1)
    print('Done Sleeping')

t1=threading.Thread(target=do_something)
t2=threading.Thread(target=do_something)

t1.start()
t2.start()

t1.join()
t2.join()

finish=time.perf_counter()

print("Seconds:",finish-start)
