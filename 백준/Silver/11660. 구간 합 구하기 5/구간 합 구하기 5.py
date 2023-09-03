# 구간 합 구하기 5
import sys
n, m = map(int, sys.stdin.readline().strip().split())

og_list = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(n)]
sm_list = [[0] * n for _ in range(n)]

# 합 배열 채우기
for r in range(n):
    for c in range(n):
        # 0, 0
        if r == 0 and c == 0:
            sm_list[r][c] = og_list[r][c]
        # 0, n / n, 0
        if r == 0 and c != 0:
            sm_list[r][c] = sm_list[r][c-1] + og_list[r][c]
            sm_list[c][r] = sm_list[c-1][r] + og_list[c][r]
        # 나머지. 0열 제외
        elif c != 0:
            sm_list[r][c] = sm_list[r-1][c] + sm_list[r][c-1] - sm_list[r-1][c-1] + og_list[r][c]

# 답 출력하기
for a in range(m):
    x1, y1, x2, y2 = map(int, sys.stdin.readline().strip().split())
    x1 -= 1
    y1 -= 1
    x2 -= 1
    y2 -= 1

    if x2 == 0 and y2 == 0:     # 0, 0 이면
        print(sm_list[x2][y2])
    elif x1 == 0 and y1 == 0:   # 작은 배열이 0,0 이면 그대로
        print(sm_list[x2][y2])
    elif x2 == 0 and y2 != 0:
        print(sm_list[x2][y2] - sm_list[x1][y1-1])  # ok
    elif x2 != 0 and y2 == 0:
        print(sm_list[x2][y2] - sm_list[x1-1][y1])  # ok
    elif x1 == 0 and y1 != 0:
        print(sm_list[x2][y2] - sm_list[x2][y1 - 1])
    elif y1 == 0 and x1 != 0:
        print(sm_list[x2][y2] - sm_list[x1 - 1][y2])
    else:
        print(sm_list[x2][y2] - sm_list[x1-1][y2] - sm_list[x2][y1-1] + sm_list[x1-1][y1-1])