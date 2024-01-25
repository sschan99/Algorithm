import sys


def main():
    N, M = map(int, (sys.stdin.readline().split()))
    rows = []
    ones = []
    for i in range(M):
        rows.append(list(map(int, (sys.stdin.readline().split()))))
        for j in range(N):
            if rows[-1][j] == 1:
                ones.append((i, j))

    answer = 0
    while ones:
        new_ones = []
        for onei, onej in ones:
            # print(onei, onej, ones)
            if onei > 0 and rows[onei - 1][onej] == 0:
                rows[onei - 1][onej] = 1
                new_ones.append((onei - 1,onej))
            if onei < M - 1 and rows[onei + 1][onej] == 0:
                rows[onei + 1][onej] = 1
                new_ones.append((onei + 1,onej))
            if onej > 0 and rows[onei][onej - 1] == 0:
                rows[onei][onej - 1] = 1
                new_ones.append((onei,onej - 1))
            if onej < N - 1 and rows[onei][onej + 1] == 0:
                rows[onei][onej + 1] = 1
                new_ones.append((onei,onej + 1))
        # print(rows)
        # print(ones)
        ones = new_ones
        if ones:
            answer += 1

    for row in rows:
        if 0 in row:
            print(-1)
            return
    print(answer)


if __name__ == "__main__":
    main()
