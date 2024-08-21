def int_to_n(i, n):
    ALP = ['A', 'B', 'C', 'D', 'E', 'F']
    if i == 0:
        return '0'
    
    res = ''
    while i > 0:
        if i % n >= 10:
            res += ALP[i % n - 10]
        else:
            res += str(i % n)
        i //= n
        
    return res[::-1]

def solution(n, t, m, p):
    answer = ''
    # n진법의 수를 t*m 개 만든다. -> range(t*m)의 십진법 수를 n진법으로 만든다
    # 만들면서 하나의 스트링으로 결합한다.
    # 차례에 따라 출력한다.
    comp = ''
    for i in range(t * m):
        comp += int_to_n(i, n)
    
    for j in range(p - 1, t * m, m):
        answer += comp[j]
    
    return answer