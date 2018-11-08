# Fibonacci numbers module
# 可以使用如下的一些引入方式
# import fibo
# from fibo import fib, fib2
# from fibo import *
# import fibo as fib
# from fibo import fib as fibonacci


def fib(n):    # write Fibonacci series up to n
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()


def fib2(n):   # return Fibonacci series up to n
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a+b
    return result


if __name__ == "__main__":
    import sys
    fib(int(sys.argv[1]))
