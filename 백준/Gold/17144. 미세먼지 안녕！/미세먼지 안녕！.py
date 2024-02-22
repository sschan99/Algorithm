import sys
input = sys.stdin.readline

def main():
    r, c, t = map(int, input().split())
    matrix = []
    machine_index = []
    for i in range(r):
        row = list(map(int, input().split()))
        if row[0] == -1:
            machine_index.append(i)
        matrix.append(row)

    for _ in range(t):
        # 미세먼지 확산
        added_matrix = [[0] * c for _ in range(r)]
        for x in range(r):
            for y in range(c):
                num = matrix[x][y]
                if -1 <= num < 5:
                    continue
                temp = num // 5
                for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    nx, ny = x + dx, y + dy
                    if not (0 <= nx < r and 0 <= ny < c):
                        continue
                    if ny == 0 and nx in machine_index:
                        continue
                    added_matrix[x][y] -= temp
                    added_matrix[nx][ny] += temp
        for x in range(r):
            for y in range(c):
                if added_matrix[x][y]:
                    matrix[x][y] += added_matrix[x][y]
        # 공기청정기 작동
        for i in range(machine_index[0] - 1, 0, -1):
            matrix[i][0] = matrix[i - 1][0]
        for i in range(c - 1):
            matrix[0][i] = matrix[0][i + 1]
        for i in range(machine_index[0]):
            matrix[i][c - 1] = matrix[i + 1][c - 1]
        for i in range(c - 1, 1, -1):
            matrix[machine_index[0]][i] = matrix[machine_index[0]][i - 1]
        matrix[machine_index[0]][1] = 0
        for i in range(machine_index[1] + 1, r - 1):
            matrix[i][0] = matrix[i + 1][0]
        for i in range(c - 1):
            matrix[r - 1][i] = matrix[r - 1][i + 1]
        for i in range(r - 1, machine_index[1], -1):
            matrix[i][c - 1] = matrix[i - 1][c - 1]
        for i in range(c - 1, 1, -1):
            matrix[machine_index[1]][i] = matrix[machine_index[1]][i - 1]
        matrix[machine_index[1]][1] = 0

    # 남아있는 미세먼지의 양
    print(sum(map(sum, matrix)) + 2)

if __name__ == '__main__':
    main()