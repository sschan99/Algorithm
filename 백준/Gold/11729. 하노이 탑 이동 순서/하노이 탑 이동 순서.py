n = int(input())

dp = [0]
for _ in range(n):
    dp.append(dp[-1] * 2 + 1)
print(dp[-1])

def hanoi(start, dest, height):
    if height == 1:
        print(start, dest)
        return

    nums = [1, 2, 3]
    nums.remove(start)
    nums.remove(dest)
    prev_dest = nums.pop()

    hanoi(start, prev_dest, height - 1)
    print(start, dest)
    hanoi(prev_dest, dest, height - 1)

hanoi(1, 3, n)