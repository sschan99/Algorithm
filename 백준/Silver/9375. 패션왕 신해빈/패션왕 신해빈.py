import collections
import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    counter = collections.defaultdict(int)
    for _ in range(n):
        a, b = input().split()
        counter[b] += 1
    result = 1
    for i in counter.values():
        result *= i + 1
    print(result - 1)
