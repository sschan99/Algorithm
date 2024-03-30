import sys
input = sys.stdin.readline

def main():
    n = int(input())
    arr = list(map(int, input().split()))
    
    temp = float('inf')
    answer = (0, 0)
    i, j = 0, n - 1
    while i < j:
        alt = abs(arr[j] + arr[i])
        if temp > alt:
            temp = alt
            answer = (arr[i], arr[j])
        if arr[j] + arr[i] > 0:
            j -= 1
        else:
            i += 1
    print(*answer)

if __name__ == '__main__':
    main()