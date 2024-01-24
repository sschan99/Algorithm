import sys

input = sys.stdin.readline

def cal(num_str):
    return len(num_str) + abs(N - int(num_str))

N = int(input())
M = int(input())
buttons = set(i for i in range(10))
if M:
    for x in input().split():
        buttons.remove(int(x))

result = abs(N - 100)

for i in range(1_000_000):
    num_str = str(i)
    for digit in num_str:
        if int(digit) not in buttons:
            break
    else:
        result = min(result, cal(num_str))

print(result)