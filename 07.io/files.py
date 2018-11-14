import json

filepath = '/Users/wentao/workspace/pystudy/pytutorial/07.io/workfile'
wfilepath = '/Users/wentao/workspace/pystudy/pytutorial/07.io/workfile_towrite'

with open(filepath) as f:
    read_data = f.read()

f.closed

f = open(filepath, 'r')

f.read()
f.read()
f.readline()

f.close()

with open(filepath, 'r') as f:
    for line in f:
        print(line, end='')

with open(filepath, 'r') as f:
    allines = list(f)
    print(allines)

with open(filepath, 'r') as f:
    print(f.readlines())

with open(wfilepath, 'rb+') as f:
    print(f.write(b'0123456789abcdef'))
    print(f.seek(5))
    print(f.read(1))
    print(f.seek(-3, 2))
    print(f.read(1))

# json
json_file = '/Users/wentao/workspace/pystudy/pytutorial/07.io/workfile_json'
f = open(json_file, 'w+')

jsonstr = json.dumps([1, 'simple', 'list'])

f.write(jsonstr)

f.close()

f = open(json_file, 'r')
x = json.load(f)
print(x)
f.close()
