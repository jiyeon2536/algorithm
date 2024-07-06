def solution(X, Y):
    x = [0] * 10
    y = [0] * 10

    for i in X:
        x[int(i)] += 1

    for j in Y:
        y[int(j)] += 1
    
    same = []
    for k in range(10):
        same.append(min(x[k], y[k]))
    
    if sum(same) == 0:
        return '-1'
    
    ans = ''
    for idx, t in enumerate(same):
        ans += str(idx) * t
    
    ans = ''.join(sorted(ans, reverse=True)) 
    
    if ans[0] == '0':
        return '0'
    return ans