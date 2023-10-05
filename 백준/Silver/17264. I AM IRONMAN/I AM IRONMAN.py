# i am ironman

import sys
input = sys.stdin.readline

n, p = map(int, input().strip().split())    # 총게임횟수, 해킹해서 얻은플레이어정보수
w, l, g = map(int, input().strip().split())    # 이길때 + 질때 - 목표점
w_list = []
l_list = []

score = 0
for i in range(p):
    name, w_or_l = input().strip().split()
    if w_or_l == 'W':
        w_list.append(name)
    else:
        l_list.append(name)

check = 0
for i in range(n):
    counterpart = input().strip()
    if counterpart in w_list:
        score += w
        if score >= g:
            check = 1
            break
    else:
        score -= l
        score = max(score, 0)

if check == 1:
    print("I AM NOT IRONMAN!!")
else:
    print("I AM IRONMAN!!")