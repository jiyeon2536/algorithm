d = [(1, 0), (0, 1), (-1, -1)]

def solution(n):
    # 정사각 배열을 만든다
    init = [[0] * n for _ in range(n)]
    
    length = n * (n + 1) // 2
    r, c = 0, 0
    j = 0
    
    for i in range(1, length + 1):        
        init[r][c] = i
        
        if i == length:
            break
            
        while True:
            nr = r + d[j][0]
            nc = c + d[j][1]
        
            if nr < 0 or nc < 0 or nr >= n or nc >= n or nr < nc or init[nr][nc] != 0:
                j = (j + 1) % 3
        
            else:
                r = nr
                c = nc
                break
        
    return [elem for arr in init for elem in arr if elem != 0]