from os import path

filedir = path.dirname(path.realpath('__file__'))


team = 'angels'

filename = path.join(filedir, 'teams/' + team + '.csv')
with open(filename, 'r') as f:
    text = f.read()
    result = []
    for line in text.splitlines():
        result.append(tuple(line.split(",")))
    
print(result[0])
print()
print(result[1:3])
