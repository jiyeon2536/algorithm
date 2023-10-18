# 알바생 강호

import sys
input = sys.stdin.readline
n = int(input())

tips = []
for i in range(n):
    tip = int(input())
    tips.append(tip)

tips.sort(reverse=True)

total = 0
# 인덱스만큼을 뺀다
for idx, val in enumerate(tips):
    to_add = val - idx
    if to_add > 0:
        total += to_add

print(total)