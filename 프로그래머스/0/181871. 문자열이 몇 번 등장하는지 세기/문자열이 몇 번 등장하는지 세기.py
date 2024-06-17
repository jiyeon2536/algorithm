def solution(myString, pat):
    answer = 0
    s = 0
    e = len(pat)
    while e <= len(myString):
        if myString[s:e] == pat:
            answer += 1
        s += 1
        e += 1
    
    return answer