


def fib(n):
    if n==1 or n==2 :
        return 1
    return fib(n-1)+fib(n-2)

print(fib(10))


def factorial (n):
    if n==1 :
        return 1
    return n*factorial(n-1)


print(factorial(40))




def reverse (s):
    if s=="":
        return ""
    return s[-1]+reverse(s[:-1])


print(reverse("hi its ahmad reverse this string ok ?"))



