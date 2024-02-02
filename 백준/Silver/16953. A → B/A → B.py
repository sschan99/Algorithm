def main():
    a, b = map(int, input().split())

    q = [a]
    count = 1

    while q:
        nq = []
        count += 1
        for x in q:
            for nx in (x * 2, x * 10 + 1):
                if nx == b:
                    return count
                if nx > b:
                    continue
                nq.append(nx)
        q = nq

    return -1

if __name__ == "__main__":
    print(main())