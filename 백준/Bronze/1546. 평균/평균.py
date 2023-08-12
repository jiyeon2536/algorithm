N = int(input())

scores = list(map(int, input().split()))

m = 0  # 최대 점수 찾기
for score in scores:
    if score > m:
        m = score

sum_new = 0
for s in scores:
    sum_new += (s / m * 100)

print(sum_new / N)

