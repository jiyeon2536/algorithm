# 최소 스패닝 트리
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
    # 엣지 uvw 로 합쳐주고
    for u in range(1, V+1):
        for v, w in graph[u]:
            edges.append((u, v, w))
    # 소트
    edges.sort(key=lambda x: x[2])
    MST = []    # 최소 신장 트리를 반환할 리스트 만들기

    # 발생하지 않으면 합쳐줌
    for u, v, w in edges:
        if find(u) == find(v):
            continue
        else:
            MST.append((u, v, w))
            union(u, v)

    return MST


import sys
V, E = map(int, sys.stdin.readline().rstrip().split())
# 연결 상태
graph = [[] for _ in range(V+1)]

for i in range(E):
    a, b, c = map(int, sys.stdin.readline().rstrip().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

parents = [i for i in range(V+1)]   # 1번부터 v번까지

MST = kruskal(graph)

total_cost = 0

for n1, n2, cost in MST:
    total_cost += cost

print(total_cost)