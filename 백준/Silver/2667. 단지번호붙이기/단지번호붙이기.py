# 단지번호 붙이기
import sys
from collections import deque
n = int(sys.stdin.readline().strip())

town = [list(sys.stdin.readline().strip()) for _ in range(n)]

di = [0, 0, 1, -1]
dj = [1, -1, 0, 0]

need_visit = deque()
cnt_ls = []

for i in range(n):
    for j in range(n):
        # 한 단지에 연결된 곳 개수 세기
        if town[i][j] == '1':
            cnt = 1
            town[i][j] = '0'  # 방문 표시
            need_visit.append((i, j))
            while need_visit:
                tmp = need_visit.popleft()
                x = tmp[0]
                y = tmp[1]
                for k in range(4):
                    ni = x + di[k]
                    nj = y + dj[k]
                    if 0 <= ni < n and 0 <= nj < n and town[ni][nj] == '1':
                        town[ni][nj] = '0'
                        cnt += 1
                        need_visit.append((ni, nj))
            cnt_ls.append(cnt)

cnt_ls.sort()

print(len(cnt_ls))
for i in range(len(cnt_ls)):
    print(cnt_ls[i])


