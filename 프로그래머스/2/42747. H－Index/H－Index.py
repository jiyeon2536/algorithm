def solution(citations):
    h = len(citations)
    
    while h > 0:
        cnt = 0
        for c in citations:
            if c >= h:
                cnt += 1
        if cnt >= h:
            break
        h -= 1
    
    return h