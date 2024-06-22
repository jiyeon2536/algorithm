def solution(s):
    answer = ''
    index = 0
    for ch in s.lower():
        index += 1
        if ch == ' ':
            index = 0
        if index % 2 == 0:
            answer += ch
        elif index % 2:
            answer += ch.upper()
    
    
    
    return answer