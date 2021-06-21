import queue

# q= queue.Queue()
# q.put(5)
#
# print(q.get())
# print(q.empty())
#
# for i in range (5):
#     q.put(i)
#
#
# while not q.empty():
#     print(q.get(),end = '  ')

import queue
import time
import threading


def putting_thread (q):
    while True :
        print('starting thread ')
        time.sleep(10)
        q.put(5)
        print('put something ')


q= queue.Queue()
t=threading.Thread(target=putting_thread(),args=(q,),daemon=True)
t.start()
