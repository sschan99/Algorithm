import sys
input = sys.stdin.readline

def main():
    n = int(input())
    arr = sorted(map(int, input().split()))
    result = (arr[0], arr[-1])
    left = 0
    right = n - 1
    while left < right:
        alt = (arr[left], arr[right])
        s = sum(alt)
        if abs(sum(result)) > abs(s):
            result = alt
        if s < 0:
            left += 1
        elif s > 0:
            right -= 1
        else:
            break
    print(*result)

if __name__ == '__main__':
    main()
