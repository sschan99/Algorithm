line = input()
bomb = list(input())
size = len(bomb)
stack = []

for char in line:
    stack.append(char)
    if stack[-size:] == bomb:
        for _ in range(size):
            stack.pop()

print(''.join(stack) if stack else 'FRULA')