# 여행 가자
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
    else:
        parents[px] = py

# 유니온 파인드로 연결해서
# 마지막 줄 입력 요소의 앞뒤가 서로 연결됐는지 확인하면 됨
import sys
n = int(sys.stdin.readline().strip())   # 전체 도시 수
m = int(sys.stdin.readline().strip())   # 여행 계획에 속한 도시 수

parents = [i for i in range(0, n+1)]    #

for i in range(1, n+1):     # n개의 줄에 주어지는 연결정보
    data = list(map(int, sys.stdin.readline().strip().split()))
    for j in range(n):
        if data[j] == 1:
            union(i, j+1)

route = list(map(int, sys.stdin.readline().split()))

res = 0
for i in range(len(route)-1):
    if find(route[i]) != find(route[i+1]):
        res = -1

if res == -1:
    print('NO')
else:
    print('YES')