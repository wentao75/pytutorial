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
