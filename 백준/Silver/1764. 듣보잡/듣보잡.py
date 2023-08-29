# 듣보잡
n, m = map(int, input().split())

unheard = [input() for _ in range(n)]
unseen = [input() for _ in range(m)]

res = sorted(list(set(unheard) & set(unseen)))

print(len(res))
for i in res:
    print(i)