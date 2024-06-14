def solution(myString, pat):
    answer = 0
    p = ''
    for i in pat:
        if i == 'A':
            p += 'B'
        else:
            p += 'A'
    return int(p in myString)