from itertools import chain

di = [1, 0, -1, 0]
dj = [0, 1, -1, -1]

def solution(n):
    answer = [[0] * (_+1) for _ in range(n)]
    total = sum([i + 1 for i in range(n)])
    cnt = 1
    
    now_i, now_j = 0, 0
    answer[now_i][now_j] = 1
    dir_idx = 0

    while cnt < total:
        nxt_i, nxt_j = now_i + di[dir_idx], now_j + dj[dir_idx]
        
        if 0 <= nxt_i < n and 0 <= nxt_j <= nxt_i and answer[nxt_i][nxt_j] == 0:
            cnt += 1 
            answer[nxt_i][nxt_j] = cnt
            now_i, now_j = nxt_i, nxt_j
        else:
            dir_idx = (dir_idx + 1) % 4
        
    return list(chain(*answer))