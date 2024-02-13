import sys
input = sys.stdin.readline

def main():
    n = int(input())
    a = list(map(int, input().split()))
    dp = [0] * n

    for i in range(n):
        temp = 0
        for j in range(i):
            if a[j] < a[i] and temp < dp[j]:
                temp = dp[j]
        dp[i] = temp + 1
    
    print(max(dp))

if __name__ == '__main__':
    main()