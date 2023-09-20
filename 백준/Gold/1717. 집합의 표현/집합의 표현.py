# 집합의 표현
def find(x):
    if parents[x] == x:
        return x
    else:
        parents[x] = find(parents[x])
        return parents[x]

def union(x, y):
    px = find(x)
    py = find(y)

    if px == py:
        return
    if px != py:
        parents[px] = py

import sys
sys.setrecursionlimit(100000)
# n + 1 개의 집합
# m은 입력으로 주어지는 연산의 개수
n, m = map(int, sys.stdin.readline().rstrip().split())
parents = [i for i in range(n + 1)]

for i in range(m):
    oper, a, b = map(int, sys.stdin.readline().rstrip().split())
    if oper == 0:
        union(a, b)
    elif oper == 1:
        if find(a) == find(b):
            print("YES")
        else:
            print("NO")
