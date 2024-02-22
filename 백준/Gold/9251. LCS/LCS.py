from collections import defaultdict
import sys
input = sys.stdin.readline

def main():
    a = input().strip()
    a_len = len(a)
    b = input().strip()
    b_len = len(b)

    dp = [[0] * b_len for _ in range(a_len)]

    flag = False
    for i in range(a_len):
        if a[i] == b[0]:
            flag = True
        if flag:
            dp[i][0] = 1
    flag = False
    for j in range(b_len):
        if a[0] == b[j]:
            flag = True
        if flag:
            dp[0][j] = 1
    
    for i in range(1, a_len):
        for j in range(1, b_len):
            if a[i] == b[j]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    print(dp[-1][-1])

if __name__ == '__main__':
    main()