n, m = map(int, input().split())

board = [input() for _ in range(n)]

white_board = ['WBWBWBWB','BWBWBWBW','WBWBWBWB','BWBWBWBW','WBWBWBWB','BWBWBWBW','WBWBWBWB','BWBWBWBW']
black_board = ['BWBWBWBW','WBWBWBWB','BWBWBWBW','WBWBWBWB','BWBWBWBW','WBWBWBWB','BWBWBWBW','WBWBWBWB']
# 얼마나 다른지 체크하고

w_difference = []
b_difference = []
w_cnt = 0
b_cnt = 0

for i in range(n-8 + 1):
    for j in range(m-8 + 1):
        for r in range(8):
            for c in range(8):
                if board[i+r][j+c] != white_board[r][c]:
                    w_cnt += 1
                if board[i+r][j+c] != black_board[r][c]:
                    b_cnt += 1
        w_difference.append(w_cnt)
        b_difference.append(b_cnt)
        w_cnt = 0
        b_cnt = 0

print(min(min(w_difference), min(b_difference)))

