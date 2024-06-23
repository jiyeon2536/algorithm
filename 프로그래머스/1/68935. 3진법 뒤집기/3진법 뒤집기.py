def solution(n):
    answer = 0
    
    tri = ''
    while n >= 3:
        tri += str(n % 3)
        n = n // 3
    tri += str(n)
    
    for i, v in enumerate(tri):
        answer += int(v) * (3 ** (len(tri) - i - 1))
    
    return answer