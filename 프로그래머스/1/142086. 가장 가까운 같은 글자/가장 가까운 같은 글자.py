def solution(s):
    # 딕셔너리를 만들건데
    answer = []
    key = {}
    for i, ch in enumerate(s):
        if ch not in key:
            key[ch] = i
            answer.append(-1)
        else:
            answer.append(i - key[ch])
            key[ch] = i
    return answer