import heapq
from collections import defaultdict, deque

def solution(cacheSize, cities):
    deq = deque() # 가장 오래된 값을 꺼내는 용도
    cache = defaultdict(int)

    def check_cache(x):
        result = 1 if x in cache else 5
        
        deq.append(x)
        cache[x] += 1
        
        while len(cache) > cacheSize:
            v = deq.popleft()
            cache[v] -= 1
            if cache[v] == 0:
                del cache[v]
        
        return result

    answer = 0
    for city in cities:
        answer += check_cache(city.lower())
    return answer