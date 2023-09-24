# n과 m (4)
n, m = map(int, input().split())

board = [-1] * m    # m개의 숫자를 고를 곳

def nqueen(row, last):  # 마지막에 고른거
    if row == m:
        print(*board)
        return
    for col in range(last, n+1):
        board[row] = col
        nqueen(row + 1, col)

nqueen(0, 1)