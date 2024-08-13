import math
def solution(n,a,b):
    answer = 1
    
    while a > 0 and b > 0:
        if (abs(a - b) == 1 and min(a, b) % 2):
            break
        a = math.ceil(a / 2)
        b = math.ceil(b / 2)
        answer += 1
        
    return answer