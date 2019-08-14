def fib(n):
    if n == 1 or n == 2:
        return 1
    return fib(n-1) + fib(n-2)

num = int(input("How many fibonacci numbers do you want to generate: "))

def fib2(n):
    a,b = 1,1
    for i in range(n-1):
        a,b = b, a+b
    return a

for i in range(1,num):
    print(fib2(i))

