# jack 짧게 풀어봅시다
import sys
n, m = map(int, sys.stdin.readline().strip().split())
cards = list(map(int, sys.stdin.readline().strip().split()))

sm = []
for i in range(n):
    for j in range(n):
        for k in range(n):
            if (i != j and j != k and i != k) and (cards[i] + cards[j] + cards[k]) <= m:
                sm.append(cards[i] + cards[j] + cards[k])
print(max(sm))