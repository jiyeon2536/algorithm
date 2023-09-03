# herd sums
import sys
n = int(sys.stdin.readline())

# 투 포인터
sm = 1
cnt = 1

st_idx = 1
end_idx = 1

while end_idx < n:
    if sm == n:
        cnt += 1
        sm -= st_idx
        st_idx += 1
        end_idx += 1
        sm += end_idx
    elif sm < n:
        end_idx += 1
        sm += end_idx
    elif sm > n:
        sm -= st_idx
        st_idx += 1

print(cnt)


