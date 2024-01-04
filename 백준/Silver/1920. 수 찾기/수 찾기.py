_n = input()
nums = set(map(int, input().split()))
_m = input()
for num in map(int, input().split()):
    print(1 if num in nums else 0)