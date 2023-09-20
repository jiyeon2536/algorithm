# virtual friends
def find(x):
    if parent[x] == x:
        return x
    else:
        parent[x] = find(parent[x])
        return parent[x]


def union(x, y):
    px = find(x)
    py = find(y)

    if px == py:
        return

    if px != py:
        parent[px] = py
        cnt[py] = cnt[px] + cnt[py]
        cnt[px] = cnt[py]


import sys
t = int(sys.stdin.readline().rstrip())
for tc in range(t):
    f = int(sys.stdin.readline().rstrip())
    parent = {}
    cnt = {}
    for i in range(f):
        u, v = sys.stdin.readline().rstrip().split()
        if u not in parent:
            parent[u] = u
            cnt[u] = 1
        if v not in parent:
            parent[v] = v
            cnt[v] = 1
        union(u, v)
        print(cnt[find(u)])
