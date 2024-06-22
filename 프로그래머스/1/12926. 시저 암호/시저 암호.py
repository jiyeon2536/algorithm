def solution(s, n):
    answer = ''
    for ch in s:
        if ch == ' ':
            answer += ch
            continue
        if ch.islower():
            if ((ord(ch) + n) > ord('z')):
                answer += chr((ord(ch) + n) - 26)
            else:
                answer += chr((ord(ch) + n))       
        else:
            if ((ord(ch) + n) > ord('Z')):
                answer += chr((ord(ch) + n) - 26)
            else:
                answer += chr((ord(ch) + n))
    return answer