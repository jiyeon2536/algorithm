def solution(msg):
    answer = []
    dictionary = {chr(i):i-64 for i in range(ord('A'), ord('Z') + 1)}
    index = 27
    ws, we = 0, 1
    # 정해지지 않은 것 : w의 길이.
    # 사전에 없는 첫 단어가 사전에 들어갈 (w + c) 인 것임!
    while we <= len(msg):
        if msg[ws:we] in dictionary:
            we += 1
        else:
            dictionary[msg[ws:we]] = index
            answer.append(dictionary[msg[ws:we - 1]]) # c빼고
            ws = we - 1  # c가 다시 시작점이 됨.
            we = ws + 1
            index += 1
    
    # 후처리
    answer.append(dictionary[msg[ws:we]])
    
    return answer