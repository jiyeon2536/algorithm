# 중복 빼고 정렬하기
import sys
n = int(sys.stdin.readline().strip())
# 카운팅으로 한번만 뽑기
nums = list(map(int, sys.stdin.readline().strip().split()))
counting = [0 for i in range(2001)]
for i in nums:
    i = i + 1000
    if counting[i] != 0:
        continue
    counting[i] += 1

for i in range(len(counting)):
    if counting[i] == 1:
        print(i-1000, end=' ')
