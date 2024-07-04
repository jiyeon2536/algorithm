def solution(s, skip, index):
    answer = ''
    
    for ch in s:
        plus = 0 # 넘어간 횟수
        res = ord(ch)
        
        while plus < index:
            res += 1
            # 현재 캐릭터가 뛰어넘어야 한다면 횟수로 세지 않고 그냥 넘김
            if chr((res - ord('a')) % 26 + ord('a')) not in skip:
                plus += 1
            
        answer += chr((res - ord('a')) % 26 + ord('a'))
        
    return answer