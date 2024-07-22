def solution(n):
    answer = n + 1
    one_n = bin(n)[2:].count('1')
    
    while answer <= 1000001:
        if one_n == bin(answer)[2:].count('1'):
            break
        answer += 1
    
    return answer