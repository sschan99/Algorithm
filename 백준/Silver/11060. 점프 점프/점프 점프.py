from collections import deque

def main():
    n = int(input())
    jump = list(map(int, input().split()))
    if n == 1:
        return 0

    queue = deque()
    queue.append((0, 0))
    visited = [False] * n
    visited[0] = True

    while queue:
        index, count = queue.popleft()
        if index + jump[index] >= n - 1:
            return count + 1
        for i in range(1, jump[index] + 1):
            if visited[index + i]:
                continue
            visited[index + i] = True
            queue.append((index + i, count + 1))
    
    return -1

print(main())