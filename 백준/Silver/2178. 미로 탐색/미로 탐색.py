# 미로 탐색
import sys
from collections import deque
n, m = map(int, sys.stdin.readline().strip().split())

maze = [list(sys.stdin.readline().strip()) for _ in range(n)]
visited = [[0] * m for _ in range(n)]
# 왼쪽 상단에서 시작해서 오른쪽 하단으로 이동하는 데 최소

need_visit = deque()

di = [0, 0, 1, -1]
dj = [1, -1, 0, 0]

need_visit.append((0, 0))
visited[0][0] = 1
while need_visit:
    tmp = need_visit.popleft()
    i = tmp[0]
    j = tmp[1]
    for k in range(4):
        ni = i + di[k]
        nj = j + dj[k]
        if 0 <= ni < n and 0 <= nj < m and maze[ni][nj] == '1' and visited[ni][nj] == 0:
            visited[ni][nj] = visited[i][j] + 1
            need_visit.append((ni, nj))

print(visited[n-1][m-1])