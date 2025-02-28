def rotate(r1, c1, r2, c2, matrix):
    first = matrix[r1][c1]
    min_value = first

    for i in range(r1, r2):
        matrix[i][c1] = matrix[i + 1][c1]
        min_value = min(min_value, matrix[i][c1])    
            
    for i in range(c1, c2):
        matrix[r2][i] = matrix[r2][i + 1]
        min_value = min(min_value, matrix[r2][i])    
        
    for i in range(r2, r1, -1):
        matrix[i][c2] = matrix[i - 1][c2]
        min_value = min(min_value, matrix[i][c2])
        
    for i in range(c2, c1, -1):
        matrix[r1][i] = matrix[r1][i - 1]
        min_value = min(min_value, matrix[r1][i])
    
    matrix[r1][c1 + 1] = first
    
    return min_value

def solution(rows, columns, queries):
    answer = []
    # 첫 배열 생성
    mtrx = [[(i + 1) + j * columns for i in range(columns)] for j in range(rows)]
    
    # rotate에서 돌려서 matrix를 바꾼다
    for [x1, y1, x2, y2] in queries:
        answer.append(rotate(x1 - 1, y1 - 1, x2 - 1, y2 - 1, mtrx))
    
    return answer