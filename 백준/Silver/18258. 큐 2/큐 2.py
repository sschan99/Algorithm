from collections import deque
import sys
input = sys.stdin.readline

def main():
    q = deque()
    for _ in range(int(input())):
        line = input().split()
        if line[0] == 'push':
            q.append(int(line[1]))
        elif line[0] == 'size':
            print(len(q))
        elif line[0] == 'empty':
            print(0 if q else 1)
        elif not q:
            print(-1)
        elif line[0] == 'pop':
            print(q.popleft())
        elif line[0] == 'front':
            print(q[0])
        elif line[0] == 'back':
            print(q[-1])

if __name__ == '__main__':
    main()