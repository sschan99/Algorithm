line = input()

stack = []
left = ('(', '[')
pair_dict = {')': '(', ']': '['}
value_dict = {'(': '2', '[': '3'}
prev = ''
result = []

for c in line:
    if c in left:
        stack.append(c)
        result.append('*(' if prev in left else '+')
        result.append(value_dict[c])
        prev = c
        continue
    if len(stack) == 0 or pair_dict[c] != stack.pop():
        print(0)
        exit()
    if prev not in left:
        result.append(')')
    prev = c

if stack:
    print(0)
    exit()

print(eval(''.join(result)))
