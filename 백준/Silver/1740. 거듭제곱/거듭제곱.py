answer = 0
n = bin(int(input()))[2:]
for i in range(len(n)):
    x = n[-1 - i]
    if x == '1':
        answer += 3 ** i
print(answer)