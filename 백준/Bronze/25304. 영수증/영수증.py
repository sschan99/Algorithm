x = int(input())
for _ in range(int(input())):
    a, b = map(int, input().split())
    x -= a * b
print('No' if x else 'Yes')