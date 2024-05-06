l, c = map(int, input().split())
s = sorted(input().split())

temp = []

def recursion(k, a, b):
    if len(temp) == l:
        if a >= 1 and b >= 2:
            print(''.join(temp))
        return
    
    for i in range(k, c):
        temp.append(s[i])
        if s[i] in ('a', 'e', 'i', 'o', 'u'):
            recursion(i + 1, a + 1, b)
        else:
            recursion(i + 1, a, b + 1)
        temp.pop()

recursion(0, 0, 0)