n = int(input())
div, mod = divmod(n, 5)

while div >= 0:
    if mod % 3 == 0:
        break
    div -= 1
    mod += 5

if div == -1:
    print(-1)
else:
    print(div + mod // 3)