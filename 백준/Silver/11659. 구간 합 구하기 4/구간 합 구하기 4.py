import sys
n, m = map(int, sys.stdin.readline().strip().split())
nums_ls = list(map(int, sys.stdin.readline().strip().split()))

# 합 배열 만들기
sum_ls = [0] * n
total = 0
for i in range(n):
    total += nums_ls[i]
    sum_ls[i] = total

# 출력 해야 하는 숫자 구간
for j in range(m):
    st, end = map(int, sys.stdin.readline().strip().split())
    if st > 1:
        print(sum_ls[end-1] - sum_ls[st-2])
    else:
        print(sum_ls[end-1])
