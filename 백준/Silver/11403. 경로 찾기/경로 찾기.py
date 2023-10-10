# 경로 찾기
import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
D = [[float('inf')] * n for _ in range(n)]

g = [list(map(int, input().split())) for _ in range(n)]   # 인접행렬

for i in range(n):
    for j in range(n):
        if g[i][j] == 1:
            D[i][j] = 1

for k in range(n):
    for st in range(n):
        for end in range(n):
            D[st][end] = min(D[st][end], D[st][k] + D[k][end])

for i in range(n):
    for j in range(n):
        if D[i][j] == float('inf'):
            print(0, end=' ')
        else:
            print(1, end=' ')
    print()