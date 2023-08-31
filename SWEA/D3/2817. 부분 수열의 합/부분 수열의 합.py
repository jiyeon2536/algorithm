# 부분 수열의 합

t = int(input())
for tc in range(1, t+1):
    n, k = map(int, input().split())    # 숫자 갯수 n 합이 k가 됨
    a = list(map(int, input().split()))

    res = 0
    for i in range(1 << n):
        subset1 = []
        sm = 0
        for j in range(n):
            if i & (1 << j):
                subset1.append(a[j])
                sm += a[j]
                if sm > k:
                    break
        if sm == k:
            res += 1

    print(f'#{tc} {res}')