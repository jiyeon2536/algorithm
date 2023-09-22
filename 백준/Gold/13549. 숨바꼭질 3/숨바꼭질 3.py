# 숨바꼭질 3
import sys
import heapq
n, k = map(int, sys.stdin.readline().strip().split())

min_heap = [(0, n)]      # cost, 노드     k를 향해 가야해
dist = [float('inf') for _ in range(100001)]    # 0부터  100000까지
dist[n] = 0

def move(x, i):
    if i == 0:
        return 1, x - 1
    elif i == 1:
        return 1, x + 1
    elif i == 2:
        return 0, 2 * x
# move = [(x - 1, 1), (x + 1, 1), (2 * x, 0)]

while min_heap:
    cur_cost, node = heapq.heappop(min_heap)
    if cur_cost > dist[node]:
        continue

    for i in range(3):
        w, nxt = move(node, i)
        if 0 <= nxt <= 100000:
            new_cost = cur_cost + w
            if dist[nxt] > new_cost:
                dist[nxt] = new_cost
                heapq.heappush(min_heap, (new_cost, nxt))

print(dist[k])

