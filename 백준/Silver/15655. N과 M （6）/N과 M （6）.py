# n과 m -6
n, m = map(int, input().split())
a = sorted(list(map(int, input().split())))
board = [-1] * m
visited = [False for _ in range(n)]

def nqueen(row, last):
    if row == m:
        print(*board)
        return
    for col in range(last, n):
        if visited[col] == False:
            visited[col] = True
            board[row] = a[col]
            nqueen(row + 1, col)
            visited[col] = False

nqueen(0, 0)