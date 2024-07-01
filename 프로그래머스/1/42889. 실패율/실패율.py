def solution(N, stages):
    answer = [0] * (N+2)
    stuck = [0] * (N+2)
    
    for s in stages:
        stuck[s] += 1
    
    total = [0] * (N+2)
    cur_sum = 0
    for i in range(N+1, 0 , -1):
        cur_sum += stuck[i]
        total[i] = cur_sum
    
    for j, (k, v) in enumerate(zip(stuck, total)):
        if j > N:
            continue
        if v == 0:
            continue
        answer[j] = k/v
        
    list1 = sorted(enumerate(answer), key=lambda x:x[1], reverse=True)
    
    
    return [i for [i, r] in list1 if 0 < i <= N]
    
    
    