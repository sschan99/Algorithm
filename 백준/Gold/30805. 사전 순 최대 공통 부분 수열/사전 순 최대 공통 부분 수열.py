def main():
    N = int(input())
    A = list(map(int, input().split()))
    M = int(input())
    B = list(map(int, input().split()))

    result = []

    while A and B:
        x = max(A)
        if x in B:
            result.append(x)
            A = A[A.index(x) + 1:]
            B = B[B.index(x) + 1:]
        else:
            A.remove(x)

    print(len(result))
    if result:
        print(*result)

main()