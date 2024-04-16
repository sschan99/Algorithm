import sys
input = sys.stdin.readline

def main():
    n = int(input())
    arr = sorted(map(int, input().split()))
    result = (0, 0, 0)
    result_sum = float('inf')
    for num in arr:
        left = 0
        right = n - 1
        while left < right:
            alt = (num, arr[left], arr[right])
            s = sum(alt)
            if abs(result_sum) > abs(s) and len(set(alt)) == 3:
                result = alt
                result_sum = s
            if s < 0:
                left += 1
            elif s > 0:
                right -= 1
            else:
                break
    print(*sorted(result))

if __name__ == '__main__':
    main()
