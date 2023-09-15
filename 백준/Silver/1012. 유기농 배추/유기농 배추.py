# 유기농 배추
import sys
from collections import deque
t = int(sys.stdin.readline().strip())

for _ in range(t):
    m, n, k = map(int, sys.stdin.readline().strip().split())

    di = [0, 0, 1, -1]
    dj = [1, -1, 0, 0]

    cabbages = deque()
    farm = [[0] * m for _ in range(n)]

    for i in range(k):
        x, y = map(int, sys.stdin.readline().strip().split())
        farm[y][x] = 1

    # 1인 곳마다 bfs 해서 연결된 곳을 모두 0으로 바꾼다.
    # 여전히 1이 있으면 거기서도 bfs
    # 모두가 0이 될때까지 비엪에스가 호출되는 횟수만큼을 출력하면 됨


    cnt = 0

    for i in range(n):
        for j in range(m):
            if farm[i][j] == 1:
                cabbages.append((i, j))
                cnt += 1
                while cabbages:
                    tmp = cabbages.popleft()
                    row = tmp[0]
                    col = tmp[1]
                    farm[row][col] = 0
                    for k in range(4):
                        ni = row + di[k]
                        nj = col + dj[k]
                        if 0 <= ni < n and 0 <= nj < m and farm[ni][nj] == 1:
                            farm[ni][nj] = 0
                            cabbages.append((ni, nj))

    print(cnt)
