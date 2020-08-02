data = ['aaa', 'bbb', 'ccc']

with open('scrap.csv', 'w') as f:
    f.write('START\n\n')
    for d in data:
        f.write(d + ',')
    f.write('\n\nEND')
