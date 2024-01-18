s = input()

i = s.find('-')
if i == -1:
    print(sum(map(int, s.split('+'))))
else:
    a = s[:i].replace('-', '+')
    b = s[i + 1:].replace('-', '+')
    sum_a = sum(map(int, a.split('+')))
    sum_b = sum(map(int, b.split('+')))
    print(sum_a - sum_b)