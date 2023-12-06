# 데스 나이트
import sys
input = sys.stdin.readline

di = [-2, -2, 0, 0, 2, 2]
dj = [-1, 1, -2, 2, -1, 1]

def bfs(i, j):
    need_visit = [(i, j)]
    while need_visit:
        tmp = need_visit.pop(0)
        r = tmp[0]
        c = tmp[1]
        if r == r2 and c == c2:
            break
        for k in range(6):
            ni = r + di[k]
            nj = c + dj[k]
            if 0 <= ni < N and 0 <= nj < N and visited[ni][nj] == 0:
                visited[ni][nj] = visited[r][c] + 1
                need_visit.append((ni, nj))


N = int(input())

r1, c1, r2, c2 = map(int, input().split())

visited = [[0] * N for _ in range(N)]

visited[r1][c1] = 1

bfs(r1, c1)

print(visited[r2][c2] - 1)