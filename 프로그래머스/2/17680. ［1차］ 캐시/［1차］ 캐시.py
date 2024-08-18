# from collections import deque
def solution(cacheSize, cities):
    q = []
    answer = 0
    if cacheSize == 0:
        return len(cities) * 5
    
    for city in cities:
        city = city.lower()
        if len(q) == 0:
            answer += 5
        elif city in q:
            q.pop(q.index(city))
            answer += 1
        else:
            answer += 5
            if len(q) == cacheSize: # 큐가 꽉 차있으면
                q.pop(0)
        q.append(city)
            
    return answer