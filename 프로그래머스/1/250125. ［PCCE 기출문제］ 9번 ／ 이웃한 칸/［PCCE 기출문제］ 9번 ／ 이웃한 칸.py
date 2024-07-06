def solution(board, h, w):
    di = [0, 0, 1, -1] 
    dj = [1, -1, 0, 0]
    
    n = len(board)
    
    res = 0
    for i in range(4):
        ni = h + di[i]
        nj = w + dj[i]
        if 0 <= ni < n and 0 <= nj < n and board[ni][nj] == board[h][w]:
            res += 1
    
    return res