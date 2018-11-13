import datetime
import math

# Formatted string literals
year = 2018
event = 'Christmas Day'
f'This is the {event} of {year}'

# str.format()
yes_votes = 42
no_votes = 43
percentage = yes_votes / (yes_votes + no_votes)
'{:-9} YES votes   {:2.2%}'.format(yes_votes, percentage)

# str() & repr()
s = 'Hello, world.'
str(s)
repr(s)
str(1/7)
x = 10*3.25
y = 200*200
s = 'The value of x is ' + repr(x) + ', and y is ' + repr(y) + '...'
print(s)

hello = 'hello, world\n'
hellos = repr(hello)
print(hellos)
repr((x, y, ('spam', 'eggs')))

# 转换字段
teststr = 'test1'
# test2 = 'test2'
f"repr() shows quotes: {teststr!r}; str() doesn't: {teststr!s}；ascii() is: {teststr!a}"


# 格式定义符
leftstr = 'left aligned'
rightstr = 'right aligned'
censtr = 'centered'
f'{leftstr:<30}'
f'{rightstr:>30}'
f'{censtr:^30}'
f'{censtr:*^30}'

ppi = 3.14
npi = -3.14
f'{ppi:+f}; {npi:+f}'
f'{ppi: f}; {npi: f}'
f'{ppi:-f}; {npi:-f}'

num = 42
f"int: {num:d};  hex: {num:x};  oct: {num:o};  bin: {num:b}"
f"int: {num:d};  hex: {num:#x};  oct: {num:#o};  bin: {num:#b}"
n2 = 1234567890
f'{n2:,}'

points = 19
total = 22
f"Correct answers: {(points/total):.2%}"

d = datetime.datetime(2018, 11, 11, 12, 33, 49)
f'{d:%Y-%m-%d %H:%M:%S}'

print(f'The value of pi is approximately {math.pi:.9f}.')

# 下面采用string.format()方法
print('We are the {} who say "{}!"'.format('knights', 'Ni'))
print('{0} and {1}'.format('spam', 'eggs'))
print('{1} and {0}'.format('spam', 'eggs'))
print('This {food} is {adjective}.'.format(food='spam',
                                           adjective='absolutely horrible'))
print('The story of {0}, {1}, and {other}.'.format('Bill', 'Manfred',
                                                   other='Georg'))

table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 8637678}
print('Jack: {0[Jack]:d}; Sjoerd: {0[Sjoerd]:d}; Dcab: {0[Dcab]:d}'
      .format(table))
print('Jack: {Jack:d}; Sjoerd: {Sjoerd:d}; Dcab: {Dcab:d}'.format(**table))

for x in range(1, 11):
    print('{0:2d} {1:3d} {2:4d}'.format(x, x*x, x*x*x))

# 使用手工字符串格式化方式
for x in range(1, 11):
    print(repr(x).rjust(2), repr(x*x).rjust(3), end=' ')
    # Note use of 'end' on previous line
    print(repr(x*x*x).rjust(4))
