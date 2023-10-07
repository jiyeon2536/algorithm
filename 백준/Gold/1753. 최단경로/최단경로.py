# 최단경로
import sys
import heapq
input = sys.stdin.readline
V, E = map(int, input().split())
k = int(input())    # 시작정점

graph = [[] for _ in range(V+1)]
for i in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))

dist = [float('INF') for _ in range(V+1)]
dist[k] = 0
min_heap =[(0, k)]  # dist, 정점번호

while min_heap:
    cur_cost, now_node = heapq.heappop(min_heap)
    if cur_cost > dist[now_node]:
        continue
    for nxt, w in graph[now_node]:
        new_cost = cur_cost + w
        if new_cost < dist[nxt]:
            dist[nxt] = new_cost
            heapq.heappush(min_heap, (new_cost, nxt))

for i in range(1, V+1):
    if dist[i] == float('inf'):
        print('INF')
    else:
        print(dist[i])