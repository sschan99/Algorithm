pair = {']': '[', ')': '('}

def check(string):
    stack = []
    for c in string:
        if c in ('(', '['):
            stack.append(c)
            continue
        if c in (')', ']'):
            if stack and pair[c] == stack.pop():
                continue
            print('no')
            return
    print('no' if stack else 'yes')

while True:
    string = input()
    if string == '.':
        break
    check(string)