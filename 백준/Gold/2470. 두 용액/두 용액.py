import sys
input = sys.stdin.readline

def main():
    n = int(input())
    arr = sorted(map(int, input().split()))
    result = (arr[0], arr[1])
    for num in arr:
        target = -num
        left = 0
        right = n - 1
        while left < right:
            mid = (left + right) // 2
            if arr[mid] < target:
                left = mid + 1
            else:
                right = mid
        for i in [left - 1, left, left + 1]:
            if i < 0 or n <= i:
                continue
            if arr[i] == num:
                continue
            alt = (num, arr[i])
            if abs(sum(result)) > abs(sum(alt)):
                result = alt
    print(*sorted(result))

if __name__ == '__main__':
    main()
