# n과 m (8)
n, m = map(int, input().split())
nums = sorted(list(map(int, input().split())))
board = [-1] * m

def nqueen(row, last):
    if row == m:
        print(*board)
        return
    for col in range(last, n):
        board[row] = nums[col]
        nqueen(row + 1, col)


nqueen(0, 0)