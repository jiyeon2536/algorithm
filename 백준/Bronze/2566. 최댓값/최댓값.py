table = [list(map(int, input().split())) for _ in range(9)]

# 가장 큰 값 찾기
mx_v = 0
mx_idx = (0, 0)
for i in range(9):
    for j in range(9):
        if mx_v <= table[i][j]:
            mx_v = table[i][j]
            mx_idx = (i+1, j+1)

print(mx_v)
print(*mx_idx)