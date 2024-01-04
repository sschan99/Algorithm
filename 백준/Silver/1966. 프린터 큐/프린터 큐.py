from collections import deque

def find_next(queue):
    return queue.index(max(queue))

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    priorities = deque(map(int, input().split()))

    result = 1
    next_index = find_next(priorities)
    while next_index != m:
        priorities.rotate(-next_index)
        m = (m - next_index + len(priorities)) % len(priorities)

        priorities.popleft()
        m -= 1
        
        next_index = find_next(priorities)
        result += 1
    print(result)