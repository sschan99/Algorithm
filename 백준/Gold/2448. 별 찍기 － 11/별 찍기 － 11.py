n = int(input())

def star(n):
    if n == 3:
        return ['  *  ', ' * * ', '*****']
    temp = star(n // 2)
    space = ' ' * (n // 2)
    upper_half = [space + line + space for line in temp]
    lower_half = [line + ' ' + line for line in temp]
    return upper_half + lower_half

print('\n'.join(star(n)))