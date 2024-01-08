import sys
input = sys.stdin.readline

output = [[1, 0], [0, 1]]
for i in range(2, 40 + 1):
    a1, b1 = output[i - 2]
    a2, b2 = output[i - 1]
    output.append([a1 + a2, b1 + b2])

t = int(input())
for _ in range(t):
    n = int(input())
    print(*output[n])