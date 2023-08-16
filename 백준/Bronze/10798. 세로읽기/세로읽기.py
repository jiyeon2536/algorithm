matrix = [input() for _ in range(5)]

for i in range(5):
    while True:
        if len(matrix[i]) < 15:
            matrix[i] += '*'
        else:
            break

for c in range(15):
    for r in range(5):
        if matrix[r][c] == '*':
            continue
        else:
            print(matrix[r][c], end='')
