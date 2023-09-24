# n과 m (5)
n, m = map(int, input().split())  # 길이가 m인 수열
nums = sorted(list(map(int, input().split())))

board = [-1] * m    # 선택한 거 저장할 곳
visited = [False for _ in range(n)]
def nqueen(row):
    if row == m:
        print(*board)
        return
    for col in range(n):
        if visited[col] == False:
            visited[col] = True
            board[row] = nums[col]
            nqueen(row + 1)
            visited[col] = False

nqueen(0)