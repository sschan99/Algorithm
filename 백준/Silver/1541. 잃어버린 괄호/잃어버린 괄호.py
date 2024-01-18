def sum_str(s):
    return sum(map(int, s.split('+')))

s = input()
i = s.find('-')
if i == -1:
    print(sum_str(s))
else:
    a = s[:i].replace('-', '+')
    b = s[i + 1:].replace('-', '+')
    print(sum_str(a) - sum_str(b))