# 타임머신
import sys
input = sys.stdin.readline

n, m = map(int, input().split())

edges = []
for i in range(m):
    a, b, c = map(int, input().split())
    edges.append((a, b, c))

dist = [float('inf') for _ in range(n+1)]
dist[1] = 0
for i in range(n-1):
    for st, end, w in edges:
        if dist[st] != float('inf') and dist[end] > dist[st] + w:
            dist[end] = dist[st] + w

check = False
for st, end, w in edges:
    if dist[st] != float('inf') and dist[end] > dist[st] + w:
        check = True

if check:
    print(-1)
else:
    for i in range(2, n+1):
        if dist[i] == float('inf'):
            print(-1)
        else:
            print(dist[i])
