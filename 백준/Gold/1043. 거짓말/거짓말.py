import sys
input = sys.stdin.readline

def main():
    n, m = map(int, input().split())
    know = set(map(int, input().split()[1:]))
    party_list = [set(map(int, input().split()[1:])) for _ in range(m)]
    
    excuted = [False] * (n + 1)

    while know:
        new_know = set()

        for one in know:
            if excuted[one]:
                continue
            excuted[one] = True

            for party in party_list:
                if one in party:
                    new_know.update(party)
                    party.clear()

        know = new_know

    print(sum(map(bool, party_list)))

if __name__ == "__main__":
    main()
