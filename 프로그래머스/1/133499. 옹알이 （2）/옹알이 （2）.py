def solution(babbling):
    answer = 0
    
    able = {"aya" : '0', "ye": '1', "woo" : '2', "ma" : '3'}
    for b in babbling:
        flag = True
        
        for a in able:
            b = b.replace(a, able[a])
            
        for i in range(len(b)):
            if (not b[i].isdigit()):
                flag = False
                break
            elif i > 0 and b[i - 1] == b[i]:
                flag = False
                break
            
        if flag:
            answer += 1
            
                
    return answer