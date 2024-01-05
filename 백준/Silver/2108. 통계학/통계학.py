import sys
input = sys.stdin.readline
from collections import Counter

n = int(input())
nums = [int(input()) for _ in range(n)]
nums.sort()

counter = Counter(nums)
how_many = counter.most_common(1)[0][1]
mode_list = list(filter(lambda k: counter[k] == how_many, counter.keys()))

print(round(sum(nums) / n))
print(nums[n//2])
print(mode_list[0 if len(mode_list) == 1 else 1])
print(nums[-1] - nums[0])