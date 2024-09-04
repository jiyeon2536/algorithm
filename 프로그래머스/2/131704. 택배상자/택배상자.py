def solution(order):
    answer = 0
    sub_belt = []  
    truck = [0 for _ in order]
    for i, o in enumerate(order):
        truck[o - 1] = i
    
    t_idx = 0
    
    while t_idx < len(truck): 
        if sub_belt and (sub_belt[-1] == answer):  
            sub_belt.pop()
            answer += 1
        elif (not sub_belt) or (sub_belt[-1] != answer):
            tmp = truck[t_idx]
            sub_belt.append(tmp)
            t_idx += 1
        else:
            break
            
        # print(answer)
        # print('트럭', truck, t_idx)
        # print('보조', sub_belt)
        # print('---')
        
    while sub_belt:
        if sub_belt[-1] == answer:
            sub_belt.pop()
            answer += 1
        else:
            break

    return answer