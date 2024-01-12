import sys
input = sys.stdin.readline

left = list(input().strip())
right = []

for _ in range(int(input())):
    argv = input().split()
    cmd = argv[0]
    if cmd == 'P':
        left.append(argv[1])
    elif cmd == 'L' and left:
        right.append(left.pop())
    elif cmd == 'D' and right:
        left.append(right.pop())
    elif cmd == 'B' and left:
        left.pop()

right.reverse()
print(''.join(left + right))