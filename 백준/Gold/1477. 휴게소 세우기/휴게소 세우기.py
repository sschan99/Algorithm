from math import ceil
import sys
input = sys.stdin.readline

def main():
    n, m, l = map(int, input().split())
    stop = [0] + sorted(map(int, input().split())) + [l]
    road = [stop[i + 1] - stop[i] for i in range(n + 1)]

    start, end = 1, l - 1
    while start != end:
        mid = (start + end) // 2
        need = sum(ceil(r / mid) - 1 for r in road)
        if need > m:
            start = mid + 1
        else:
            end = mid
    return start

if __name__ == '__main__':
    print(main())