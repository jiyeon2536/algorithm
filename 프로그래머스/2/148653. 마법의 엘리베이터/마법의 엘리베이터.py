def solution(storey):
    answer = 0
    
    st = list(str(storey))
    n = len(st)
    
    for i in range(n - 1, -1, -1):
        tmp = int(st[i])
        if tmp < 5:
            answer += tmp
        elif tmp > 5:
            answer += (10 - tmp)
            if i > 0:
                st[i - 1] = str(int(st[i - 1]) + 1)
            else: # 맨앞이면
                answer += 1
        else:  # 5인 경우에
            if i > 0:
                former = int(st[i - 1])
                
                if former < 5:
                    answer += tmp #내림
                    
                if former >= 5:
                    answer += (10 - tmp)
                    st[i - 1] = str(former + 1)
            else:  
                answer += tmp
                    
    return answer