# 이분 그래프
def dfs(node):
    global is_bi
    visited[node] = True
    for nxt in graph[node]:
        if visited[nxt] == False:
            visited[nxt] = True
            team[nxt] = (team[node] + 1) % 2
            dfs(nxt)
        elif team[nxt] == team[node]:
            is_bi = False


import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline
k = int(input())    # 테스트 케이스
for tc in range(k):
    v, e = map(int, input().split())    # 정점 개수, 간선 개수
    graph = [[] for _ in range(v+1)]    # 인접 리스트
    for i in range(e):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)


    visited = [False for _ in range(v+1)]   # 방문 체크
    team = [0 for _ in range(v+1)]  # 팀 확인
    is_bi = True


    for i in range(1, v+1):
        if is_bi:
            dfs(i)
        else:
            break

    if is_bi:
        print('YES')
    else:
        print('NO')
