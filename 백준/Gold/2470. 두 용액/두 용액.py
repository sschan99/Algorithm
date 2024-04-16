import sys
input = sys.stdin.readline

def main():
    n = int(input())
    arr = sorted(map(int, input().split()))
    result = (float('inf'), 0, 0)
    left = 0
    right = n - 1
    while left < right:
        alt = (arr[left] + arr[right], arr[left], arr[right])
        if abs(result[0]) > abs(alt[0]):
            result = alt
        if alt[0] < 0:
            left += 1
        elif alt[0] > 0:
            right -= 1
        else:
            break
    print(result[1], result[2])

if __name__ == '__main__':
    main()
