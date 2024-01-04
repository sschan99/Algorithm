from collections import Counter

input()
counter = Counter(input().split())
input()
print(*map(lambda x: counter[x], input().split()))