# 숫자카드 2
import sys
n = int(sys.stdin.readline())
cards = sys.stdin.readline().split()
m = int(sys.stdin.readline())
nums = sys.stdin.readline().split()

a = {}
for i in range(n):
    if cards[i] not in a:
        a[cards[i]] = 1
    else:
        a[cards[i]] += 1

res = []
for j in range(m):
    if nums[j] in a:
        res.append(a[nums[j]])
    else:
        res.append(0)

print(*res)