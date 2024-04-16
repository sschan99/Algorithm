import sys
input = sys.stdin.readline

def main():
    n = int(input())
    arr = sorted(map(int, input().split()))
    result = (float('inf'), 0, 0, 0)
    for i in range(n - 2):
        left = i + 1
        right = n - 1
        while left < right:
            s = arr[i] + arr[left] + arr[right]
            if abs(result[0]) > abs(s):
                result = (s, arr[i], arr[left], arr[right])
            if s < 0:
                left += 1
            else:
                right -= 1
    print(*result[1:])

if __name__ == '__main__':
    main()
