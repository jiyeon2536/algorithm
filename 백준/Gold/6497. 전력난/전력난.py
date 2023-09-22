# dark roads
import sys
def find(x):
    if parents[x] == x:
        return x
    else:
        parents[x] = find(parents[x])
        return parents[x]

def union(x, y):
    px = parents[x]
    py = parents[y]

    if px == py:
        return
    else:
        parents[px] = py


def kruskal(graph):
    edges = []

    for u in range(m):
        for v, w in graph[u]:
            edges.append((u, v, w))

    edges.sort(key=lambda x : x[2])
    MST = []    # 최소신장트리 저장할 곳

    for u, v, w in edges:
        if find(u) != find(v):
            MST.append((u, v, w))
            union(u, v)

    return MST


while True:
    m, n = map(int, sys.stdin.readline().split())     # 노드 m 에지수 n
    if m == 0 and n == 0:
        break       # 0, 0이 들어오면 시스템 종료
    graph = [[] for _ in range(m)]  # 0부터 시작하는 엣지이므로
    origin_cost = 0
    for i in range(n):
        x, y, z = map(int, sys.stdin.readline().split())
        origin_cost += z
        graph[x].append((y, z))     # 연결점, 가중치 길이
        graph[y].append((x, z))

    parents = [i for i in range(m)]
    MST = kruskal(graph)    # 최소신장트리의 연결만 남기고 나머지는 다 지울거임

    total_cost = 0

    for n1, n2, cost in MST:
        total_cost += cost

    print(origin_cost - total_cost)

