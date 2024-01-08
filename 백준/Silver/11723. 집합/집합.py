import sys
input = sys.stdin.readline

b = 0
MASK = 0xFFFFF

def one_bit(x):
    return 1 << (x - 1)

for _ in range(int(input())):
    argv = input().split()
    cmd = argv[0]
    x = int(argv[1]) if len(argv) > 1 else 0
    if cmd == 'add':
        b |= one_bit(x)
    elif cmd == 'remove':
        b &= one_bit(x) ^ MASK
    elif cmd == 'check':
        print(1 if b & one_bit(x) else 0)
    elif cmd == 'toggle':
        b ^= one_bit(x)
    elif cmd == 'all':
        b = MASK
    elif cmd == 'empty':
        b = 0
    else:
        raise ValueError
