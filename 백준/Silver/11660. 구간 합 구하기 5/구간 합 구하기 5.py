# 구간 합 구하기 5 _ 인덱스 바꿔서 다시 풀기
import sys
input = sys.stdin.readline
n, m = map(int, input().strip().split())
og_list = [[0] * (n + 1)]
sm_list = [[0] * (n + 1) for _ in range(n+1)]

for i in range(n):
    a_row = [0] + [int(x) for x in input().split()]
    og_list.append(a_row)

# 합 배열 만들기
for r in range(1, n+1):
    for c in range(1, n+1):
        sm_list[r][c] = sm_list[r][c-1] + sm_list[r-1][c] - sm_list[r-1][c-1] + og_list[r][c]

# 답 구하기
for ans in range(m):
    x1, y1, x2, y2 = map(int, input().strip().split())
    print(sm_list[x2][y2] - sm_list[x1-1][y2] - sm_list[x2][y1-1] + sm_list[x1-1][y1-1])