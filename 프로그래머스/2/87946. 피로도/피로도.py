from itertools import permutations
def solution(k, dungeons):
    answer = -1
    perm = list(permutations(dungeons))
    
    for p in perm:
        remain = k
        tmp_ans = 0
        for [mn, rq] in p:
            if remain >= mn:
                tmp_ans += 1
                remain -= rq
        answer = max(tmp_ans, answer)
            
    return answer