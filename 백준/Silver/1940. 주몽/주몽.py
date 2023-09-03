# 주몽
import sys
n = int(sys.stdin.readline().strip())    # 재료의 개수
m = int(sys.stdin.readline().strip())    # 갑옷을 만드는 데 필요한 수
nums = sorted(list(map(int, sys.stdin.readline().strip().split())))
# 7 5 4 3 2 1

st_idx = 0
end_idx = (n-1)

cnt = 0

while st_idx < end_idx:
    total = nums[st_idx] + nums[end_idx]
    if total == m:
        cnt += 1
        st_idx += 1
        end_idx -= 1
    elif total < m:
        st_idx += 1
    elif total > m:
        end_idx -= 1

print(cnt)
