def solution(line):
    pos, answer = [], []
    n = len(line)
    
    mx_x = mx_y = -int(1e15)
    mn_x = mn_y = int(1e15)
    
    for i in range(n):
        a, b, e = line[i]
        for j in range(i+1, n):
            c, d, f = line[j]
            
            if (a*d - b*c) == 0:
                continue
                
            x = ((b*f) - (e*d)) / ((a*d) - (b*c))
            y = ((e*c) - (a*f)) / ((a*d) - (b*c))
            
            if x == int(x) and y == int(y):
                pos.append([x, y])
                mx_x = max(x, mx_x)
                mx_y = max(y, mx_y)
                mn_x = min(x, mn_x)
                mn_y = min(y, mn_y)
        
    # 길이
    len_x = int(mx_x - mn_x) + 1
    len_y = int(mx_y - mn_y) + 1
    
    base = [['.'] * len_x for _ in range(len_y)]
    # 이제 pos 돌면서 base에 별을 하나씩 찍는다
    
    for [ox, oy] in pos:
        star_x = int(ox - mn_x)
        star_y = int(mx_y - oy)
        base[star_y][star_x] = '*'
    
    
    return [''.join(b) for b in base]
    