import sys
input = sys.stdin.readline

def main():
    n = int(input())
    table = [list(map(int, input().split())) for _ in range(n)]

    using = [False] * 9
    order = []

    def cal():
        i = 0
        j = 0
        score = 0
        while i < n:
            out = 0
            inning = table[i]
            base_1 = base_2 = base_3 = False
            while out < 3:
                run = inning[order[j]]
                if run == 1:
                    score += base_3
                    base_1, base_2, base_3 = True, base_1, base_2
                elif run == 2:
                    score += base_3 + base_2
                    base_1, base_2, base_3 = False, True, base_1
                elif run == 3:
                    score += base_3 + base_2 + base_1
                    base_1, base_2, base_3 = False, False, True
                elif run == 4:
                    score += base_3 + base_2 + base_1 + 1
                    base_1 = base_2 = base_3 = False
                else:
                    out += 1
                j = (j + 1) % 9
            i += 1
        return score

    def re():
        if len(order) == 9:
            return cal()
            
        if len(order) == 3:
            order.append(0)
            result = re()
            order.pop()
            return result
        
        results = []
        for i in range(1, 9):
            if using[i]:
                continue
            using[i] = True
            order.append(i)
            results.append(re())
            using[i] = False
            order.pop()
        return max(results)
        
    print(re())

if __name__ == "__main__":
    main()
