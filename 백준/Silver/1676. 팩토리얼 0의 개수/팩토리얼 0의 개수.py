n = int(input())

def cal(x, factor):
    result = 0
    while x % factor == 0:
        x //= factor
        result += 1
    return result

two_count = 0
five_count = 0
for i in range(1, n + 1):
    two_count += cal(i, 2)
    five_count += cal(i, 5)

print(min(two_count, five_count))