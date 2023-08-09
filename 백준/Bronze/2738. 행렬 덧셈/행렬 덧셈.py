N, M = map(int, input().split())

matrix_a = [list(map(int, input().split())) for _ in range(N)]
matrix_b = [list(map(int, input().split())) for _ in range(N)]


for i in range(N):
    matrix_res = []
    for j in range(M):
        matrix_res.append(matrix_a[i][j] + matrix_b[i][j])
    print(*matrix_res)