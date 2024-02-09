from collections import deque
import sys
input = sys.stdin.readline

def main():
    for _ in range(int(input())):
        p = input().strip()
        n = int(input())
        array = input().strip()

        q = deque(array[1:-1].split(',') if n else [])

        reverse = False
        for c in p:
            if c == 'R':
                reverse = not reverse
                continue
            if not q:
                print('error')
                break
            if reverse:
                q.pop()
            else:
                q.popleft()
        else:
            if reverse:
                q.reverse()
            print('[' + ','.join(q) + ']')

if __name__ == '__main__':
    main()