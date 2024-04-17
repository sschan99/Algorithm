import sys
input = sys.stdin.readline

def main():
    n = int(input())
    a = [0] + list(map(int, input().split()))
    d = [0]
    x = [0]

    for i in range(1, n + 1):
        left = 0
        right = len(x) - 1
        while left < right:
            mid = (left + right + 1) // 2
            if x[mid] < a[i]:
                left = mid
            else:
                right = mid - 1
        j = left
        d.append(j + 1)
        if j + 1 < len(x):
            x[j + 1] = a[i]
        else:
            x.append(a[i])
    print(max(d))

if __name__ == '__main__':
    main()
