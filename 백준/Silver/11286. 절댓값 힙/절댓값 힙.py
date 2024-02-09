import heapq
import sys
input = sys.stdin.readline

def main():
    h = []
    for _ in range(int(input())):
        x = int(input())
        if x:
            heapq.heappush(h, (abs(x), 1 if x > 0 else -1))
            continue
        if not h:
            print(0)
            continue
        a, b = heapq.heappop(h)
        print(a * b)

if __name__ == '__main__':
    main()