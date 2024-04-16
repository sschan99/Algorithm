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
        if abs(sum(result)) > abs(sum(alt)):
            result = alt
        if sum(alt) < 0:
            left += 1
        elif sum(alt) > 0:
            right -= 1
        else:
            break
    print(*result)

if __name__ == '__main__':
    main()
