nums = [int(input()) for _ in range(5)]
print(sum(n if n >= 40 else 40 for n in nums) // 5)