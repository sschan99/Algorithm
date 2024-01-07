input()
string = input()

result = 0
squared = 1
for i in range(len(string)):
    n = ord(string[i]) - 96
    result += n * squared
    squared *= 31

print(result % 1234567891)