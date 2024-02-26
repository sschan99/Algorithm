from math import ceil
import sys
input = sys.stdin.readline

def main():
    n, m, l = map(int, input().split())
    stop = [0] + sorted(map(int, input().split())) + [l]
    road = [stop[i + 1] - stop[i] for i in range(n + 1)]

    def get_need(x):
        return sum(ceil(r / x) - 1 for r in road)

    start, end = 1, l - 1
    while start != end:
        mid = (start + end) // 2
        if get_need(mid) > m:
            if start == mid:
                break
            start = mid
        else:
            end = mid
    return end

if __name__ == '__main__':
    print(main())