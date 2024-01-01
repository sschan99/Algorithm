d = {'1 2 3 4 5 6 7 8': 'ascending', '8 7 6 5 4 3 2 1': 'descending'}

s = input()

if s in d:
    print(d[s])
else:
    print('mixed')