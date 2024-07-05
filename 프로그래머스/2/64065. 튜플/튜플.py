def solution(s):
    
    # 총 개수
    s = s.split('},')
    answer = [0] * len(s)

    new_arr = [el.replace('{', '').replace('}', '') for el in s]
    
    # new_arr 를 길이 순서대로 정렬한다.
    new_arr = sorted(new_arr, key= lambda x : len(x), reverse=True)
        
    for i in range(len(s) - 1):
        answer[len(s) - i - 1] = int(list(set(new_arr[i].split(',')) - set(new_arr[i+1].split(',')))[0])
    
    answer[0] = int(new_arr[-1])
    
    return answer