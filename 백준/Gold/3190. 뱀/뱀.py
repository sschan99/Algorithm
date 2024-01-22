import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
k = int(input())

apple = set()
for _ in range(k):
    x, y = map(int, input().split())
    apple.add((x - 1, y - 1))

l = int(input())

turn = deque()
for _ in range(l):
    x, c = input().split()
    turn.append((int(x), 1 if c == 'D' else -1))

snake = deque([(0, 0)])
body = set(snake)
sec = i = 0
d = [(0, 1), (1, 0), (0, -1), (-1, 0)]

while True:
    sec += 1
    
    x = snake[-1][0] + d[i][0]
    y = snake[-1][1] + d[i][1]
    head = (x, y)

    if not (0 <= x < n and 0 <= y < n):
        break
    if head in body:
        break

    snake.append(head)
    body.add(head)

    if head in apple:
        apple.remove(head)
    else:
        tail = snake.popleft()
        body.remove(tail)

    if turn and turn[0][0] == sec:
        i = (i + turn[0][1]) % 4
        turn.popleft()

print(sec)
