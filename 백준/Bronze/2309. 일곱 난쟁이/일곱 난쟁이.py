a = sorted(int(input()) for _ in range(9))
s = sum(a) - 100
for i in range(8):
    for j in range(i + 1, 9):
        if a[i] + a[j] == s:
            for k in range(9):
                if k in (i, j):
                    continue
                print(a[k])
            exit()