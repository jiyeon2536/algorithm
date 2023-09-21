# 덩치
# 이중 포문 돌면서 누군가 나보다 키도 크고 몸무게도 크다면 +1 한다.
# 다 돌고 카운트를 넣는다
# 카운트 초기화한다
import sys
n = int(sys.stdin.readline().rstrip())
w_ls = []
h_ls = []
for i in range(n):
    w, h = map(int, sys.stdin.readline().rstrip().split())
    w_ls.append(w)
    h_ls.append(h)

for i in range(n):  # 지금 나
    cnt = 1
    for j in range(n):  # 다른 사람들과 비교
        if i == j:
            continue
        else:
            if w_ls[i] < w_ls[j] and h_ls[i] < h_ls[j]:     # 나보다 키도 크고 몸무게도 큰 사람이 있다면
                cnt += 1
    print(cnt, end=' ')


