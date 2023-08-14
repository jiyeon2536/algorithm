N, K = map(int, input().split())

factor = []
for i in range(1, N+1):
    if N % i == 0:
        factor.append(i)

if len(factor) >= K:
    print(factor[K-1])
else:
    print('0')