from bisect import bisect_left
import sys
input = sys.stdin.readline

def main():
    n = int(input())
    a = list(map(int, input().split()))

    d = []
    x = [0]

    for i in range(n):
        j = bisect_left(x, a[i])
        d.append(j)
        if j == len(x):
            x.append(a[i])
        else:
            x[j] = a[i]

    print(max(d))

if __name__ == '__main__':
    main()
