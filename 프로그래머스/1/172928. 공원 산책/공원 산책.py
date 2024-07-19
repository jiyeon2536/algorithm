def solution(park, routes):
    answer = [0, 0]
    
    dire = {
        'E': (0, 1),
        'S': (1, 0),
        'W': (0, -1),
        'N': (-1, 0)
    }
    
    n, m = len(park), len(park[0])
    for i in range(n):
        for j in range(m):
            if park[i][j] == 'S':
                answer = [i, j]
    
    for r in routes:
        tmp = r.split()
        togo = 0  # 이동을 반복하는 횟수
        flag = True
        while togo <= int(tmp[1]):
            ni = answer[0] + int(dire[tmp[0]][0] * togo)
            nj = answer[1] + int(dire[tmp[0]][1] * togo)
            togo += 1
            if ni < 0 or ni >= n or nj < 0 or nj >= m or park[ni][nj] == 'X':
                flag = False
                break

        if flag:
            answer = [ni, nj]
        
    return answer