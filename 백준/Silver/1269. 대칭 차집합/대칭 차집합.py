# 대칭 차집합
na, nb = map(int, input().split())
a = set(map(int, input().split()))
b = set(map(int, input().split()))
res = set((a - b) | (b - a))
print(len(res))
