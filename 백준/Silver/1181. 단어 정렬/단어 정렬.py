words = set()
for _ in range(int(input())):
    words.add(input())
result = sorted(words, key=lambda x: (len(x), x))
for word in result:
    print(word)