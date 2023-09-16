# avoid the lakes
import sys
from collections import deque
n, m, k = map(int, sys.stdin.readline().strip().split())

farm = [[0] * m for _ in range(n)]  # 원행렬 0, 1 만들어 감
lakes = [[0] * m for _ in range(n)]  # 표시 행렬 / visited 로 쓰면 됨
submerged = deque()  # 체크를 해야 하는 아이들
for i in range(k):
    r, c = map(int, sys.stdin.readline().strip().split())
    farm[r-1][c-1] = 1
    submerged.append((r-1, c-1))


di = [0, 0, 1, -1]
dj = [1, -1, 0, 0]

need_visit = deque()

mx = 0
for i in submerged:
    row = i[0]
    col = i[1]
    cnt = 1
    if lakes[row][col] == 0:
        lakes[row][col] = 1
        need_visit.append((row, col))
        while need_visit:
            tmp = need_visit.popleft()
            row = tmp[0]
            col = tmp[1]
            for k in range(4):
                ni = row + di[k]
                nj = col + dj[k]
                if 0 <= ni < n and 0 <= nj < m and farm[ni][nj] == 1 and lakes[ni][nj] == 0:
                    lakes[ni][nj] = 1
                    need_visit.append((ni, nj))
                    cnt += 1
    mx = max(mx, cnt)


print(mx)