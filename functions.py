def fib(n):
    """打印一个Fibonacci数列（兔子数列），一直到最大数n"""
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b

    print()


fib(2000)

f = fib

f(1000)


def fib2(n):
    """返回一个包含Fibonacci数列到最大数n的数组"""
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a+b

    return result


f100 = fib2(100)
f100


# 更多的方法定义
# 默认参数值
def ask_ok(prompt, retries=4, reminder="请重试！"):
    while True:
        ok = input(prompt)
        if ok in ('y', 'ye', 'yes'):
            return True
        if ok in ('n', 'no', 'nop', 'nope'):
            return False

        retries = retries - 1
        if retries < 0:
            raise ValueError('无效的用户输入')
        print(reminder)


ask_ok('请输入：')


# 默认值是一个可变对象，例如：数组，字典，或者很多类的实例
# 默认值在定义发生的时刻固定下来，如果是可变对象，那么在后续使用过程中会一直保持变化
def f(a, L=[]):
    L.append(a)
    return L


print(f(1))
print(f(2))
print(f(3))


# 如果要避免默认值在不同使用中共享而相互影响，最好设置为空
def ff(a, L=None):
    if L is None:
        L = []
    L.append(a)
    return L


print(ff(1))
print(ff(2))
print(ff(3))


def parrot(voltage, state='a stiff', action='voom', type='Norwegian Blue'):
    print("-- This parrot wouldn't", action, end=' ')
    print("if you put", voltage, "volts through it.")
    print("-- Lovely plumage, the", type)
    print("-- It's", state, "!")
    print("-" * 60)


# 下面都是正确的调用方式，使用参数名=数值的方式
parrot(1000)                                          # 1 positional argument
parrot(voltage=1000)                                  # 1 keyword argument
parrot(voltage=1000000, action='VOOOOOM')             # 2 keyword arguments
parrot(action='VOOOOOM', voltage=1000000)             # 2 keyword arguments
parrot('a million', 'bereft of life', 'jump')         # 3 positional arguments
parrot('a thousand', state='pushing up the daisies')  # 1 positional, 1 keyword

# 下面是无效的调用方式
parrot()                     # required argument missing
# parrot(voltage=5.0, 'dead')  # non-keyword argument after a keyword argument
parrot(110, voltage=220)     # duplicate value for the same argument
parrot(actor='John Cleese')  # unknown keyword argument
