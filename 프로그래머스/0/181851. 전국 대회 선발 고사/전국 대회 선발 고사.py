def solution(rank, attendance):
    # 새 배열을 돌면서 어탠이 트루인거 세개를 뽑고
    # 계산
    c = []
    arr = sorted([[r, i] for i, r in enumerate(rank)])
    
    for [_, i] in arr:
        if len(c) == 3:
            break
        if attendance[i]:
            c.append(i)
            
    return 10000 * c[0] + 100 * c[1] + c[2]