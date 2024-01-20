import heapq
import sys
input = sys.stdin.readline

n, m = map(int, input().split())

h = []
for x in map(int, input().split()):
    heapq.heappush(h, -x)

need = m
height = -heapq.heappop(h)
tree_count = 1
while h:
    next_tree = -heapq.heappop(h)
    diff = height - next_tree
    if diff * tree_count < need:
        need -= diff * tree_count
        height = next_tree
        tree_count += 1
    else:
        div, mod = divmod(need, tree_count)
        height -= div + 1 if mod else div
        break
if not h:
    div, mod = divmod(need, tree_count)
    height -= div + 1 if mod else div

print(height)