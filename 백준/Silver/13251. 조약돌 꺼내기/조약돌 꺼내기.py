# 조약돌 꺼내기
# n 개 중에 k개를 골랐을때 모두 같은 색일 확률
# n개 중에 k개를 고르는 경우의 수 분에 모두 같은 색일 경우의 수
import sys
input = sys.stdin.readline
m = int(input())    # 색상 갯수
stones = list(map(int, input().split()))    # 색상별 돌수
k = int(input())   # 고르는 갯수
n = sum(stones)     # 전체 돌 갯수

res = 0
# 첫번째 색 돌만 뽑을 경우
for i in range(m):
    tmp = 1
    for j in range(k):  # k개 고름
        tmp *= (stones[i] - j) / (n - j)
    res += tmp

print(res)