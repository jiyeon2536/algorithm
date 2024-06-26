def solution(n, m, section):
    answer = 1
    st = section[0]
    
    for s in section:
        end = st + m
        # 안덮히는 구역에 있으면
        if end <= s:
            answer += 1
            st = s
        
    return answer