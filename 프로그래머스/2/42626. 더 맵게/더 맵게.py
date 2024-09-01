import heapq

def mixed(least, sec_to_least):
    return least + (sec_to_least * 2)


def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    
    while scoville[0] < K:
        
        if len(scoville) < 2:
            return -1
        
        heapq.heappush(scoville, mixed(heapq.heappop(scoville), heapq.heappop(scoville)))
        
        answer += 1
    
    return answer