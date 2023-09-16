# 아기 상어
import sys
from collections import deque
n, m = map(int, sys.stdin.readline().strip().split())

cell = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(n)]

di = [1, 0, -1, 0, 1, -1, 1, -1]
dj = [0, 1, 0, -1, 1, -1, -1, 1]

sharks = deque()

for i in range(n):
    for j in range(m):
        if cell[i][j] == 1:
            sharks.append((i, j))

while sharks:
    tmp = sharks.popleft()
    r = tmp[0]
    c = tmp[1]
    for k in range(8):
        ni = r + di[k]
        nj = c + dj[k]
        if 0 <= ni < n and 0 <= nj < m and cell[ni][nj] == 0:
            cell[ni][nj] = cell[r][c] + 1
            sharks.append((ni, nj))

mx = 0
for i in range(n):
    for j in range(m):
        mx = max(mx, cell[i][j])

print(mx - 1)  # 출발이 1이므로 빼줌