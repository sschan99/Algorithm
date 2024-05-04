n = int(input())
result = []

def hanoi(start, dest, height):
    if height == 1:
        result.append((start, dest))
        return 1

    nums = [1, 2, 3]
    nums.remove(start)
    nums.remove(dest)
    prev_dest = nums.pop()

    x = hanoi(start, prev_dest, height - 1) + 1
    result.append((start, dest))
    x += hanoi(prev_dest, dest, height - 1)
    return x

print(hanoi(1, 3, n))
for start, dest in result:
    print(start, dest)