def recursion(n):
    if n == 3:
        return ['***', '* *', '***']
    temp = recursion(n // 3)
    result = []
    for line in temp:
        result.append(line * 3)
    for line in temp:
        result.append(line + ' ' * (n // 3) + line)
    for line in temp:
        result.append(line * 3)
    return result

for line in recursion(int(input())):
    print(line)