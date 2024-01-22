def z(n, r, c):
    if n == 1:
        return 2 * r + c
    
    half = 2 ** (n - 1)

    count = 0
    if r >= half:
        count += 2 * half ** 2
        r -= half
    if c >= half:
        count += half ** 2
        c -= half
    
    return count + z(n - 1, r, c)

print(z(*map(int, input().split())))