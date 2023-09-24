# n과 m
n, m = map(int, input().split())

visited = [False for _ in range(n+1)]   # 가로로 비지티드 배열 만들 곳
board = [-1] * m    # m 개를 실제로 고르는 곳

def nqueen(row, last):  # 마지막으로 골라진 숫자
    if row == m:
        print(*board)
        return
    for col in range(last, n+1):  # 이전에 뽑힌 값부터 n사이에서
        if visited[col] == False:
            visited[col] = True
            board[row] = col
            nqueen(row + 1, col)     # 한 칸 더 내려가서 고른다
            visited[col] = False

nqueen(0, 1)

