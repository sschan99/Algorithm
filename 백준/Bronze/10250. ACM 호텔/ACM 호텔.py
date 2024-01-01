def check_in(h, w, n):
    div, mod = divmod(n, h)
    if mod == 0:
        return str(h) + str(div).zfill(2)
    return str(mod) + str(div + 1).zfill(2)

for _ in range(int(input())):
    room = check_in(*map(int, input().split()))
    print(room)