import sys

n = int(sys.stdin.readline())
cards = sys.stdin.readline().split()
m = int(sys.stdin.readline())
nums = sys.stdin.readline().split()
check = dict()
for i in range(m):
    check[nums[i]] = 0

for j in range(n):
    if cards[j] in check:
        check[cards[j]] = 1

print(*list(check.values()))
