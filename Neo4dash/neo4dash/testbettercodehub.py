def fib(n):
    if n <= 1:
        return n
    else:
        return (fib(n-1) + fib(n-2))

def show():
    i = 0
    while(1):
        i = i + 1
        print(fib(i))

show()
