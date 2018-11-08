for n in range(2, 20):
    for x in range(2, n):
        if n % x == 0:
            print(n, 'equals', x, '*', n//x)
            break
    else:
        print(n, 'is a prime number')

for num in range(2, 10):
    if num % 2 == 0:
        print("Found an even number", num)
        continue
    print("Found a odd number", num)


# Busy-wait for keyboard interrupt
while True:
    pass


# This is commonly used for creating minimial classes
class MyEmptyClass:
    pass


# Remember to implement this
def initlog(*args):
    pass
