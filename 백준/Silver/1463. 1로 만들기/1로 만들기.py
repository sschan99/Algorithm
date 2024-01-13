from collections import deque

x = int(input())
queue = deque([(x, 0)])
visited = [False] * (x + 1)

while queue:
    num, count = queue.popleft()
    if visited[num]:
        continue
    visited[num] = True
    if num == 1:
        print(count)
        break
    if num % 3 == 0:
        queue.append((num // 3, count + 1))
    if num % 2 == 0:
        queue.append((num // 2, count + 1))
    queue.append((num - 1, count + 1))