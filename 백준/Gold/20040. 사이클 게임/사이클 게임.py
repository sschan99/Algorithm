import sys
input = sys.stdin.readline

def main():
    n, m = map(int, input().split())
    group = [i for i in range(n)]
    member = {i: [i] for i in range(n)}
    for i in range(1, m + 1):
        a, b = map(int, input().split())

        group_num = [group[a], group[b]]
        group_num.sort(key=lambda x: len(member[x]))
        small_group, big_group = group_num

        if small_group == big_group:
            return i

        for c in member[small_group]:
            group[c] = big_group
            member[big_group].append(c)
        del member[small_group]

    return 0

if __name__ == '__main__':
    print(main())