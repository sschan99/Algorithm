import sys

input = sys.stdin.readline

N = int(input())
M = int(input())
buttons = [str(i) for i in range(10)]
if M != 0:
    for x in input().split():
        buttons.remove(x)

def cal(num_str):
    return len(num_str) + abs(N - int(num_str))

results = [abs(N - 100)]

def run(num_str):
    results.append(cal(num_str))
    if len(num_str) == len(str(N)) + 1:
        return
    for x in buttons:
        run(num_str + x)

for x in buttons:
    run(x)

print(min(results))