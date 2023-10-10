#  플로이드
import sys
input = sys.stdin.readline
n = int(input())    # 도시수
m = int(input())    # 버스수

D = [[float('inf')] * (n+1) for _ in range(n+1)]


for i in range(m):
    a, b, c = map(int, input().split())
    D[a][b] = min(D[a][b], c)


for i in range(1, n+1):
    D[i][i] = 0

for k in range(1, n+1):
    for st in range(1, n+1):
        for end in range(1, n+1):
            D[st][end] = min(D[st][end], D[st][k] + D[k][end])

for i in range(1, n+1):
    for j in range(1, n+1):
        if D[i][j] == float('inf'):
            print(0, end=' ')
        else:
            print(D[i][j], end=' ')
    print()