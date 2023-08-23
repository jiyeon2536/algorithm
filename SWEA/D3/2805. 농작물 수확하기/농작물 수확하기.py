# 농작물 수확하기 별찍기로 풀기
t = int(input())
for tc in range(1, t+1):
    n = int(input())
    farm = [input() for _ in range(n)]

    # 로직
    res = 0
    for i in range(n//2 + 1):
        for j in range(n):
            if j == (n//2 - i):
                for k in range(2*i + 1):
                    res += int(farm[i][j+k])

    for r in range(n//2 + 1, n+1):
        for c in range(n):
            tmp = r - (n // 2)
            if c == tmp:
                for p in range(n-2*tmp):
                    res += int(farm[r][c+p])
                    
    # 출력
    print(f'#{tc} {res}')