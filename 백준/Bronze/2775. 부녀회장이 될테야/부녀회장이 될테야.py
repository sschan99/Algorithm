matrix = [[0 for _ in range(15)] for _ in range(15)]

for i in range(15):
    matrix[0][i] = i
    matrix[i][1] = 1

for i in range(1, 15):
    for j in range(2, 15):
        matrix[i][j] = matrix[i-1][j] + matrix[i][j-1]

for _ in range(int(input())):
    print(matrix[int(input())][int(input())])
