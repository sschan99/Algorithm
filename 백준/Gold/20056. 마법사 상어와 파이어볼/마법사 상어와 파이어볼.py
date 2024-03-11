import sys
input = sys.stdin.readline

DIRECTION = ((-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1))
EVEN_DIRS = (0, 2, 4, 6)
ODD_DIRS = (1, 3, 5, 7)

def main():
    N, M, K = map(int, input().split())
    matrix = [[[] for _ in range(N)] for _ in range(N)]
    for _ in range(M):
        r, c, m, s, d = map(int, input().split())
        matrix[r - 1][c - 1].append((m, s, d))

    for _ in range(K):
        temp = [[[] for _ in range(N)] for _ in range(N)]
        for r in range(N):
            for c in range(N):
                for m, s, d in matrix[r][c]:
                    dr, dc = DIRECTION[d]
                    nr = (r + dr * s) % N
                    nc = (c + dc * s) % N
                    temp[nr][nc].append((m, s, d))
                matrix[r][c].clear()
        for r in range(N):
            for c in range(N):
                if not temp[r][c]:
                    continue
                if len(temp[r][c]) == 1:
                    matrix[r][c].append(temp[r][c][0])
                    continue
                m_zip, s_zip, d_zip = zip(*temp[r][c])
                nm = sum(m_zip) // 5
                if nm == 0:
                    continue
                ns = sum(s_zip) // len(s_zip)
                flag = sum(d % 2 for d in d_zip) in (0, len(d_zip))
                dirs = EVEN_DIRS if flag else ODD_DIRS
                for nd in dirs:
                    matrix[r][c].append((nm, ns, nd))
    result = 0
    for r in range(N):
        for c in range(N):
            for m, s, d in matrix[r][c]:
                result += m
    print(result)

if __name__ == '__main__':
    main()