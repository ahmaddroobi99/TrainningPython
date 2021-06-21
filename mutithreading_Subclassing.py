# import time
# import threading
#
# class MyThread (threading.Thread):
#     def __init__(self , number,func, args) :
#         threading.Thread.__init__(self)
#         self.number =number
#         self.func =func
#         self.args =args
#
#
#
#
#     def run (self ):
#         print('thread{}has started'.format(self.number))
#         self.func(*self.args)
#         print('thread{} has finished'.format(self.number))
#
#
# def double (number , cycle):
#     for i  in range(cycle):
#         number+=number
#     print(number)
#
# threads_list =[]
#
# for i in range (50):
#     t =MyThread (number= i+1,func=double,args=[i,3])
#     threads_list.append(t)
#     t.start()
#
#
# for t in threads_list :
#     t.join()


import threading
import time


class MyThread(threading.Thread):
    def __init__(self, number, style, *args, **kwargs):
        super(MyThread, self).__init__(*args, **kwargs)
        self.number = number
        self.style = style

    def run(self, *args, **kwargs):
        print('thread starting')
        super(MyThread, self).run(*args, **kwargs)
        print('thread has ended')


def sleeper(num, style):
    print('we are sleeping for {} seconds as {}'.format(num, style))
    time.sleep(num)


t = MyThread(number=3, style='yellow', target=sleeper,
             args=[3, 'yellow'])

t.start()




