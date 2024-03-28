def solution(array, commands):
    answer = []
    
    # commands를 순회하면서
    # command i, j, k 를 떼어내서 가져온다.
    # 원래 어레이에 있는 -1 에서 [:] 해서
    # .sort 하고 찾아서 준다
    
    for command in commands:
        i, j, k = command
        a = sorted(array[i-1:j])
        answer.append(a[k-1])
        
    
    return answer