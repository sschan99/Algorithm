N = int(input())
M = int(input())
S = input()

result = 0
i = 0
while i < M:
    if S[i] == 'I':
        count = 0
        while i + 2 < M and S[i + 1:i + 3] == 'OI':
            count += 1
            i += 2
        result += max(count - N + 1, 0)
    i += 1
print(result)