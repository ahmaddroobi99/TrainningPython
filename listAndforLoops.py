x = [1, "two", 6 / 2]

print(x)
def f(x):
    return [x,2*x,3*x,4*x]

print(f(3))
y =f(9)
print(type(y))

print(f("AH"))


#################
#list methods
a=[1,2,3,4,5,-9,-100,99,45,75,-1,0]
b=["hi", "its ahmad","nice to concatenate with numbers ", 55]
w=a +b
print(w)
print(len(w))
print(dir(w))
print(type(w.sort))
a.sort()
print(a)
b.append("ha its new element")
print(b)
b.extend(["a","vv"])
print(b)               # the main diff between append and extend s that the first with elements the second with lists like merging


######################
#For loop

names = ["Uma", "Utta", "Ursula", "Eunice", "Unix"]
for name in names:
      print("Hi " + name + "!")


count = 1
for foo in names :
    count+=1
    print(count,foo)

print(([1, 2, 3] + ['’a’, ’b’, ’c’'] )[3])


####RAnge


for i in range(len(names)):
      print(i, names[len(names) - 1 - i])


#Tuples                #the main diff between tuples and list is mutablity you could could change lists but u couldnt for tuples
t= 1, "two", 2*1.5
print(t)
print(type  (t))
t= list(t)
print(t)
t[1]=2
print(t)


#simultanous assignment with Lists
p =[1,2,3,4,5]
i,j,k,l ,m = p
print(i,j,k,l ,m)
q =('a','b','f','e')
r= "wow"

p,q,r=r,q,p

print(p,q,r)

# fibonanaci
def fib (n):

    old,new= 0,1
    for i in range(n):
      old, new= new ,old+new
    return old

print (fib (10))
print(fib(99))

xlist = [2, 1, 3]
ylist = xlist.sort()  ## output :[1, 2, 3] None
print(xlist, ylist)


xlist4 = list(range(-3))
print(xlist4)


def f5(x, y):
    print([x, y])
    return [x, y]





print(f5(10,5))

a = 1
b = 2
xlist = [a, b, a + b]
a = 0
b = 0
print(xlist)

xlist = [3, 5, 7]
print(xlist[1] + xlist[2])


xlist = ["aa", "bb", "cc"]
for i in [2, 1, 0]:
  print(xlist[i], end=" ")


def main():
    num = eval(input("Enter a number: "))
    for i in range(3):
        num = num * 2
    print(num)
main()


s = ['a','b','c','d','e']
for i in range(len(s) - 1, -1, -1):
  print(s[i], end = " ")



print ()
###################
#nice pattern pyramid numbers

for i in range(7):
    print(" "*(7-i),end="")
    for j in range(1,i+2):
        print(j,end="")
    for j in range (i, 0 , -1):
        print (j , end="")
    print()


