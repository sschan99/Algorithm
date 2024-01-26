import sys

input = sys.stdin.readline


def main():
    M, N, H = map(int, input().split())
    tomato = []

    q = []
    result = -1

    for h in range(H):
        matrix = []
        for i in range(N):
            row = list(map(int, input().split()))
            for j in range(M):
                if row[j] == 1:
                    q.append((h, i, j))
            matrix.append(row)
        tomato.append(matrix)

    while q:
        result += 1
        nq = []
        for h, x, y in q:
            if h - 1 >= 0 and tomato[h - 1][x][y] == 0:
                tomato[h - 1][x][y] = 1
                nq.append((h - 1, x, y))
            if h + 1 < H and tomato[h + 1][x][y] == 0:
                tomato[h + 1][x][y] = 1
                nq.append((h + 1, x, y))
            if x - 1 >= 0 and tomato[h][x - 1][y] == 0:
                tomato[h][x - 1][y] = 1
                nq.append((h, x - 1, y))
            if x + 1 < N and tomato[h][x + 1][y] == 0:
                tomato[h][x + 1][y] = 1
                nq.append((h, x + 1, y))
            if y - 1 >= 0 and tomato[h][x][y - 1] == 0:
                tomato[h][x][y - 1] = 1
                nq.append((h, x, y - 1))
            if y + 1 < M and tomato[h][x][y + 1] == 0:
                tomato[h][x][y + 1] = 1
                nq.append((h, x, y + 1))
        q = nq

    for matrix in tomato:
        for row in matrix:
            if 0 in row:
                print(-1)
                return
    print(result)


if __name__ == "__main__":
    main()
