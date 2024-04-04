def solution(answers):
    result = []
    
    first = [1, 2, 3, 4, 5]
    second = [2, 1, 2, 3, 2, 4, 2, 5]
    third = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    
    scores = {
        '1': 0,
        '2': 0,
        '3': 0
    }
    
    nproblems = len(answers)
    
    for i in range(nproblems) : 
        if answers[i] == first[i % 5]:
            scores['1'] += 1
        if answers[i] == second[i % 8]:
            scores['2'] += 1
        if answers[i] == third[i % 10]:
            scores['3'] += 1
    
    v_arr = scores.values()
    mx = max(v_arr)

    
    for k, v in scores.items():
        if v == mx:
            result.append(int(k))
    
    result.sort()
        
    return result