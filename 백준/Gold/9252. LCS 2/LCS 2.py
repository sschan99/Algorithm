import sys
input = sys.stdin.readline

def main():
    s1 = list(input().strip())
    s2 = list(input().strip())
    n = len(s1)
    m = len(s2)
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    print(dp[n][m])

    temp = []
    i, j = n, m
    while dp[i][j] > 0:
        if dp[i - 1][j] == dp[i][j]:
            i -= 1
            continue
        if dp[i][j - 1] == dp[i][j]:
            j -= 1
            continue
        temp.append(s1[i - 1])
        i -= 1
        j -= 1
    temp.reverse()
    print(''.join(temp))

if __name__ == '__main__':
    main()