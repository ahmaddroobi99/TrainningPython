def find_averages(xlist):
   for inner in xlist:
       if inner:
        total = 0
        for num in inner:
           total = total + num
        print(total / len(inner))

zlist = [[20, 15, 40], [], [5, 8, 10, 15, 100], [3.14]]
find_averages(zlist)

creatures = [['dog', 'Rover', 7], ['Fred','human', 2],
  ['dog', 'Fido', 1], ['humam', 'Sally', 32]]
for species, name, age in creatures:
   if species == 'dog':
       if age <= 2:
             print(name, "is just a pup.")
       else:
            print(name, "is all grown up.")
   if species == 'humam':
          print("Hi " + name + ".")




def show_grade(score):
    if score >= 90:
           print("A")
    elif score >= 80:
           print("B")
    elif score >= 70:
           print("C")
    elif score >= 60:
           print("D")
    else:
           print("F")
show_grade(91)

show_grade(80)



def monotonic(xlist):
    for i in range(len(xlist) - 1):
        if xlist[i] < xlist[i + 1]:
             return False
    return True
data1 = [5, 3, 2, 2, 0]
data2 = [5, 2, 3, 2, 0]

print(monotonic(data1), monotonic(data2))




def is_there(names, query):
    if name in names:


        if query == name:
            return True

# print(is_there([['a','c','f'],'f']))


def swapper(xlist):                    #this is one swap in bubble sort if you need full swap you need to use another nested for loop
    for i in range(len(xlist) - 1):
        if xlist[i] > xlist[i + 1]:
    # Swap values.
             xlist[i], xlist[i + 1] = xlist[i + 1], xlist[i]
data = [5, 3, 2, 2, 0]
swapper(data)
print(data)

