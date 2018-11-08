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


#  *name, **name 参数
#  如果最后有一个**name形式的参数，这个参数将会接受除了已经匹配到正式参数之外的所有包含关键字
#  的参数；这个参数还可以搭配一个类似 *name 形式的参数，它接受一个已经匹配正式参数之外的包含
#  位置参数的tuple
def cheeseshop(kind, *arguments, **keywords):
    print("-- Do you have any", kind, "?")
    print("-- I'm sorry, we're all out of", kind)
    for arg in arguments:
        print(arg)
    print("-" * 40)
    for kw in keywords:
        print(kw, ":", keywords[kw])


cheeseshop("Limburger", "It's very runny, sir.",
           "It's really very, VERY runny, sir.",
           shopkeeper="Michael Palin",
           client="John Cleese",
           sketch="Cheese Shop Sketch")


# 任意参数列表
# 如果要接受任意数量的参数，可使用这个方式，这些参数将被组合在一个tuple中传递；其他确定的参数
# 仍然正常传递
def write_multiple_items(file, separator, *args):
    file.write(separator.join(args))


def concat(*args, sep="/"):
    return sep.join(args)


concat("earth", "mars", "venus")

concat("earth", "mars", "venus", sep=".")


# 对于已经有参数存在于list数组或者tuple结构中时，但是需要提供给函数的参数使用时，可以使用
# *操作符对解包在结构中的数据到参数列表中
list(range(3, 6))
args = [3, 6]
list(range(*args))


def parrot(voltage, state='a stiff', action='voom'):
    print("-- This parrot wouldn't", action, end=' ')
    print("if you put", voltage, "volts through it.", end=' ')
    print("E's", state, "!")


d = {"voltage": "four million", "state": "bleedin' demised", "action": "VOOM"}
parrot(**d)


# lambda表达式，用于产生一个最简短的匿名函数，通常它产生的是单个表达式语法的函数
# 例子1
def make_incrementor(n):
    return lambda x: x + n


f = make_incrementor(36)
f(0)
f(1)

# 例子2
pairs = [(1, "one"), (2, "two"), (3, "three"), (4, "four")]
pairs.sort(key=lambda pair: pair[1])
pairs


# Documentation Strings
def my_function():
    """ 这是函数的说明，这个函数用于示例，不执行其他任何操作

    函数没有任何操作执行！
    """
    pass


print(my_function.__doc__)


# 函数注释，Function Annotations
# 注释不会影响到函数的其他方面，所有的注释存储在 __annotations__ 属性中，参数在参数名后用
# 冒号定义，返回值通过在表达式最后跟 -> 定义
def f(ham: str, eggs: str = 'eggs') -> str:
    print("Annotations:", f.__annotations__)
    print("Arguments:", ham, eggs)
    return ham + ' and ' + eggs


f('spam')
