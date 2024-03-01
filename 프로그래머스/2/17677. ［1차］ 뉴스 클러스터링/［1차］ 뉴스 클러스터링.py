from collections import defaultdict

def make_multiset(string):
    multiset = set()
    counter = defaultdict(int)
    for i in range(len(string) - 1):
        a, b = string[i], string[i + 1]
        if a.isalpha() and b.isalpha():
            s = (a + b).lower()
            multiset.add(s + str(counter[s]))
            counter[s] += 1
    return multiset

def solution(str1, str2):
    ms1 = make_multiset(str1)
    ms2 = make_multiset(str2)
    if not ms1 | ms2:
        return 65536
    result = len(ms1 & ms2) / len(ms1 | ms2)
    return int(result * 65536)
    