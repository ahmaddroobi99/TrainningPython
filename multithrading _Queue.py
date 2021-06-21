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
###############################################################3
# import queue
# import time
# import threading
#
#
# def putting_thread (q):
#     while True :
#         print('starting thread ')
#         time.sleep(10)
#         q.put(5)
#         print('put something ')
#
#
# q= queue.Queue()
# t=threading.Thread(target=putting_thread(),args=(q,),daemon=True)
# t.start()


import queue
import time

q=queue.PriorityQueue()

q.put((1,'prionity 1'))
q.put((5,'prionity 5'))
q.put((3,'prionity 3'))
q.put((6,'prionity 6'))
q.put((2,'prionity 2'))
q.put((4,'prionity 4'))

for i in range (q.qsize()):
    print (q.get()[0])





