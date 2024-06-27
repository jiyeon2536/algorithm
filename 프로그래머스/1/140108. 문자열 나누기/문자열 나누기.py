def solution(s):
    answer = 0
    
    first = ''
    
    target = 0
    others = 0
    
    for ch in s :
        # 횟수가 같아지는 순간 
        if target == others:
            answer += 1
            first = ''
            target = 0
            others = 0
        # 초기화 직후
        if first == '':
            first = ch
            target += 1
        # 과정
        elif first == ch:
            target +=1
        elif first != ch:
            others += 1
        
    return answer