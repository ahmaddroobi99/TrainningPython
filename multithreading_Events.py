import time
import threading
import numpy as np
import queue



def flag ():
    time.sleep(3)
    event.set()
    print ("starting countingdown ")
    time.sleep(7)
    print("event is cleared ")
    event.clear()



def start_operation ():
     event.wait()
     while event.is_set():
         print ('starting random integer task ')
         x= np.random.randint(1,30)
         time.sleep (.5)
         if x==20:
             print ('True' )
     print("event has been cleared ,random operation stops")


event =threading.Event()
t1 =threading.Thread(target=flag)
t2= threading.Thread(target=start_operation)



t1.start()
t2.start()

# t1.join()
# t2.join()