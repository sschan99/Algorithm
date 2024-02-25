import sys
input = sys.stdin.readline

def main():
    n, L = map(int, input().split())
    x_arr = list(map(int, input().split()))

    s = sum(x_arr)
    for i in range(n - 1):
        x = x_arr[i]
        s -= x
        left, right = x - L, x + L
        if not (left < s / (n - 1 - i) < right):
            return 'unstable'
    return 'stable'

if __name__ == '__main__':
    print(main())