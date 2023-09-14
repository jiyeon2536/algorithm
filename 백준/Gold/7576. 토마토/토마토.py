# 토마토
from collections import deque
import sys
m, n = map(int, sys.stdin.readline().strip().split())

di = [-1, 1, 0, 0]
dj = [0, 0, 1, -1]

tomatoes = [[0] * m for _ in range(n)]
# 모두 익어 있는 상황 = -1 과 1 로만 있는 경우

# 익은 토마토들의 인덱스 리스트
riped = deque()

cnt = 0     # 안 익은 토마토가 있는지 없는지
for i in range(n):
    tomatoes[i] = list(map(int, sys.stdin.readline().strip().split()))
    for j in range(m):
        if tomatoes[i][j] == 1:
            riped.append((i, j))    # 시작점 저장
        elif tomatoes[i][j] == 0:
            cnt += 1

while riped:
    t = riped.popleft()
    i = t[0]
    j = t[1]
    for k in range(4):
        ni = i + di[k]
        nj = j + dj[k]
        if 0 <= ni < n and 0 <= nj < m and tomatoes[ni][nj] == 0:
            tomatoes[ni][nj] = tomatoes[i][j] + 1
            riped.append((ni, nj))

mx = 0
for i in range(n):
    if cnt == 0:
        break
    if mx == -1:
        break
    for j in range(m):
        if tomatoes[i][j] == 0:
            mx = -1
            break
        if tomatoes[i][j] > mx:
            mx = tomatoes[i][j]

if mx > 0:
    print(mx - 1)
else:
    print(mx)
