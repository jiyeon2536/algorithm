def solution(want, number, discount):
    answer = 0
    d_want = dict(zip(want, number))
    if len(discount) < 10:
        return 0
    
    st, end = 0, 9
    while end < len(discount):
        d_dis = {}
        for i in discount[st:end + 1]:
            if i in d_dis:
                d_dis[i] += 1
            else:
                d_dis[i] = 1
        if d_want == d_dis:
            answer += 1
        st += 1
        end += 1
    
    return answer