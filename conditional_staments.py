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
       if age > 2:
            print(name, "is all grown up.")
   if species == 'humam':
          print("Hi " + name + ".")
