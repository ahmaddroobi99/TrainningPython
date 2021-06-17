def find_averages(xlist):
   for inner in xlist:
       if inner:
        total = 0
        for num in inner:
           total = total + num
        print(total / len(inner))

zlist = [[20, 15, 40], [], [5, 8, 10, 15, 100], [3.14]]
find_averages(zlist)
