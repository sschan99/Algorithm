import heapq
from collections import defaultdict

def solution(cacheSize, cities):
    pq = [] # 가장 오래된 값을 꺼내는 용도
    cache = defaultdict(int)

    def check_cache(x, t):
        result = 1 if x in cache else 5
        
        heapq.heappush(pq, (t, x))
        cache[x] += 1
        
        while len(cache) > cacheSize:
            _, v = heapq.heappop(pq)
            cache[v] -= 1
            if cache[v] == 0:
                del cache[v]
        
        return result

    answer = 0
    time = 0
    for city in cities:
        answer += check_cache(city.lower(), time)
        time += 1
    return answer