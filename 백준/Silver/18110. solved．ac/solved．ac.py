import sys
input = sys.stdin.readline

def round(float):
    a, b = str(float).split('.')
    if int(b[0]) >= 5:
        return int(a) + 1
    return int(a)

n = int(input())
if n == 0:
    print(0)
    exit()

nums = sorted(int(input()) for _ in range(n))
e = round(n * 0.15)
result = round(sum(nums[e:n - e]) / (n - 2 * e))
print(result)