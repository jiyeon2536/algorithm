# 동전 0
import sys
input = sys.stdin.readline

n, k = map(int, input().split())    # 동전 종류의 수, 필요한 돈 목표

coins = []
for i in range(n):
    c = int(input())
    if c <= k:
        coins.append(c)

l = len(coins) - 1  # coins 에서 제일 큰 동전은 coins[l]
cnt = 0

while k > 0 or l >= 0:
    cnt += (k // coins[l])
    k = k % coins[l]
    l -= 1

print(cnt)

