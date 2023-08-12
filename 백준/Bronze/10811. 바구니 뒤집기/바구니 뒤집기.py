N, M = map(int, input().split())

# get buckets
buckets = []
for b in range(1, N + 1):
    buckets.append(b)

# get nums how to reverse the buckets
for m in range(M):
    i, j = map(int, input().split())
    temp = buckets[i-1:j]
    temp.reverse()
    buckets[i-1:j] = temp

print(*buckets)