import heapq
import sys
input = sys.stdin.readline

def main():
    n, k = map(int, input().split())

    jewels = sorted(tuple(map(int, input().split())) for _ in range(n))
    jewels.reverse()
    bags = sorted(int(input()) for _ in range(k))
    pq = []
    result = 0

    for c in bags:
        while jewels and jewels[-1][0] <= c:
            m, v = jewels.pop()
            heapq.heappush(pq, -v)
        if pq:
            result -= heapq.heappop(pq)

    print(result)

if __name__ == '__main__':
    main()
