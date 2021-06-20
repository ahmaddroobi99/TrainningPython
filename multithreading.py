import _thread
import threading
import time

# # Define a function for the thread
# def print_time( threadName, delay):
#    count = 0
#    while count < 5:
#       time.sleep(delay)
#       count += 1
#       print ("%s: %s" % ( threadName, time.ctime(time.time()) ))
#
# # Create two threads as follows
# try:
#    threading.start_new_thread( print_time, ("Thread-1", 2, ) )
#    threading.start_new_thread( print_time, ("Thread-2", 4, ) )
# except:
#    print ("Error: unable to start thread")
#
# while 1:
#    pass

def sleeper (n, name) :
   print('hi ,iam {} going to sleep for 5s'.format(name))
   time.sleep(n)

#
# t=threading.Thread(target=sleeper,name='thread1',args=(5,'thread1'))
#
# t.start()
# t.join()

print("hello")
print("hello")


threads_list =[]
start =time.time()
for i in range(5):
   t= threading.Thread(target=sleeper,name='thread{}'.format(i),args=(5,'thread{}'.format(i)))
   threads_list.append(t)
   t.start()
   print('{}has started'.format(t.name))



for i in threads_list :
   t.join()
end = time.time()
print('time taken:{}'.format(end-start))
print("all five tasks (Threads)ended here >>Finshied")


