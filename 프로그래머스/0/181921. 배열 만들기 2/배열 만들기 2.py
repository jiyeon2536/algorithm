def solution(l, r):
    answer = []
    for i in range(l, r+1):
        flag = 0
        for j in str(i):
            if j in '12346789':
                flag = 1
        if flag == 0:
            answer.append(i)
    return answer or [-1]