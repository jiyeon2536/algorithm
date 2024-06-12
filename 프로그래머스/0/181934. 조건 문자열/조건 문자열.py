def solution(ineq, eq, n, m):
    answer = 0
    if eq == '=':
        if ineq == '<':
            answer = (n < m) or (n == m)
        else:
            answer = (n > m) or (n == m)
    else:
        if ineq == '<':
            answer = (n < m)
        else:
            answer = (n > m)
        
    return int(answer)