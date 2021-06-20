# import threading
# import time
#
# total =4
# def creates_items():
#     global total
#     for i in range (10):
#         time.sleep(2)
#         print('added items ')
#         total += 1
#     print("creation is Done!!")
#
#
#
# def creates_items2 ():
#     global total
#     for i in range(7):
#         time.sleep(1)
#         print("Added Iem ")
#         total +=1
#     print ("Craetion is Done")
#
#
# def limits_items ():
#     global total
#     while True :
#
#         if total >5 :
#             print ('overload ')
#             total-= 3
#             print ('subtracted 3 ')
#         else :
#             time.sleep(1)
#             print('waiting')
#
#
# creator1 =threading.Thread(target=creates_items(),args=(5,))
# creator2= threading.Thread(target=creates_items2(),args=(5,))
# limitor =threading.Thread(target=limits_items(),args=(5,),daemon=True)
#
# print (limitor.isDaemon())
#
# creator1.start()
# creator2.start()
# limitor.start()
#
# print (limitor.isDaemon())
# creator1.join()
# creator2.join()
# # limitor.join()
#
#
# print("the end value of total is ::",total)


import threading
import time

total = 4


def creates_items():
    global total
    for i in range(10):
        time.sleep(2)
        print('added item')
        total += 1
    print('creation is done')


def creates_items_2():
    global total
    for i in range(7):
        time.sleep(1)
        print('added item')
        total += 1
    print('creation is done')


def limits_items():
    # print('finished sleeping')

    global total
    while True:
        if total > 5:

            print('overload')
            total -= 3
            print('subtracted 3')
        else:
            time.sleep(1)
            print('waiting')


creator1 = threading.Thread(target=creates_items)
creator2 = threading.Thread(target=creates_items_2)
limitor = threading.Thread(target=limits_items, daemon=True)

print(limitor.isDaemon())

creator1.start()
creator2.start()
limitor.start()

creator1.join()
creator2.join()

print('our ending value of total is', total)