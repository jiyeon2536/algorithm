def solution(n, lost, reserve):
    answer = 0    
    clothes = {}
    
    for i in range(1, n + 1) :
        clothes[i] = 1
    
    for l in lost:
        clothes[l] -= 1
    
    for r in reserve:
        clothes[r] += 1
    
    
    for j in range(1, n + 1):
        if j != 1 and clothes[j] == 0 and clothes[j - 1] > 1:
            clothes[j] += 1
            clothes[j - 1] -= 1
        elif j != n and clothes[j] == 0 and clothes[j + 1] > 1:
            clothes[j] += 1
            clothes[j + 1] -= 1
    
    for k in range(1, n + 1):
        if clothes[k] > 0:
            answer += 1
    
    
    return answer