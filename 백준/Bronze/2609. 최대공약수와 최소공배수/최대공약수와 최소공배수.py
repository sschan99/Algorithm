def euclidean(a, b):
    while b != 0:
        a, b = b, a % b
    return a

nums = list(map(int, input().split()))
gcd = euclidean(max(nums), min(nums))
lcm = (nums[0] // gcd) * nums[1]
print(gcd, lcm, sep='\n')