from math import inf

N, M = map(int, input().split())
matrix = [input() for _ in range(N)]

def cal_diff(str1, str2):
    return sum(str1[i] != str2[i] for i in range(8))

const = ('WBWBWBWB', 'BWBWBWBW')
def run(i, j):
    count = [0, 0]
    for n in range(8):
        line = matrix[i + n][j:j + 8]
        count[0] += cal_diff(line, const[n % 2])
        count[1] += cal_diff(line, const[(n + 1) % 2])
    return min(count)

result = inf
for i in range(N - 7):
    for j in range(M - 7):
        result = min(result, run(i, j))
print(result)