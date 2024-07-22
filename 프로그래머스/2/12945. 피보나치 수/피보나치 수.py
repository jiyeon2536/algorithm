def solution(n):    
    i = 1
    f_0, f_1 = 0, 1
    while i < n:
        f_0, f_1 = f_1, f_0 + f_1
        i += 1
        
    return f_1 % 1234567