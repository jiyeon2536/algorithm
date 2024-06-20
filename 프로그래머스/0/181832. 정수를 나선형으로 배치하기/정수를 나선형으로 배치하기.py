def solution(n):
    answer = [[0] * n for _ in range(n)]
    direction = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    
    i, j = [0, 0]
    d = 0
    for num in range(1, n*n + 1):    
        answer[i][j] = num # 해당 자리에 숫자를 넣을 것임
        ni = i + direction[d][0] # 다음 좌표
        nj = j + direction[d][1] # 다음 좌표
        if 0 <= ni < n and 0 <= nj < n and answer[ni][nj] == 0:
            # 다음 좌표가 유효하다면
            i, j = ni, nj # 다음 좌표를 넣어주고 다음 반복문으로 넘어간다
            continue
        else:
            # 유효하지 않다면
            d = (d+1) % 4 # d 값을 바꾸어서
            i += direction[d][0] # 다음 좌표값을 넣어준다
            j += direction[d][1]
        
    return answer