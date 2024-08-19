def solution(k, dungeons):
    
    def back(remain, cnt):
        nonlocal n, answer, visited
        if cnt >= answer:
            answer = cnt
        
        for i in range(n):
            if not visited[i] and remain >= dungeons[i][0]:
                visited[i] = 1
                back(remain - dungeons[i][1], cnt + 1)
                visited[i] = 0
    
    
    n = len(dungeons)
    visited = [0] * n
    answer = -1
    back(k, 0)
            
    return answer