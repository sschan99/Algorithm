import sys
input = sys.stdin.readline

s = set()

m = int(input())
for _ in range(m):
    argv = input().split()
    cmd = argv[0]
    x = int(argv[1]) if len(argv) > 1 else 0
    if cmd == 'add':
        s.add(x)
    elif cmd == 'remove':
        if x in s: s.remove(x)
    elif cmd == 'check':
        print(1 if x in s else 0)
    elif cmd == 'toggle':
        if x in s: s.remove(x)
        else: s.add(x)
    elif cmd == 'all':
        for i in range(1, 20 + 1): s.add(i)
    elif cmd == 'empty':
        s.clear()
    else:
        raise ValueError
