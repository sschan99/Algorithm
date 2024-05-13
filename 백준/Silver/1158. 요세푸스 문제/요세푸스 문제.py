from collections import deque
import sys
input = sys.stdin.readline

def main():
    n, k = map(int, input().split())
    deq = deque(range(1, n + 1))
    result = []
    while deq:
        deq.rotate(-k)
        result.append(deq.pop())
    print(f'<{", ".join(map(str, result))}>')

if __name__ == '__main__':
    main()