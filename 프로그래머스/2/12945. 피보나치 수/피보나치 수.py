def solution(n):
    answer = 0
    
    i = 1
    f_0, f_1 = 0, 1
    while i < n:
        answer = f_0 + f_1
        f_0 = f_1
        f_1 = answer
        i += 1
        
    return answer % 1234567