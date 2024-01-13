import sys
input = sys.stdin.readline

n = int(input())
step = [int(input()) for _ in range(n)]

if n <= 2:
    print(sum(step))
    exit()

max_score = [0] * n
max_score[0] = step[0]
max_score[1] = step[0] + step[1]
max_score[2] = max(step[1], max_score[0]) + step[2]

for i in range(3, n):
    max_score[i] = max(max_score[i - 3] + step[i - 1], max_score[i - 2]) + step[i]

print(max_score[n - 1])