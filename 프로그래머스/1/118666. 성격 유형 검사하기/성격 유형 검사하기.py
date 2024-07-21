def solution(survey, choices):
    answer = ''
    # 1번 지표 RT, 2번 지표 CF, 3번 지표 JM, 4번 지표 AN
    res = ['RT', 'CF', 'JM', 'AN']
    scores = {'R':0, 'T':0, 'C':0, 'F':0, 'J':0, 'M':0, 'A': 0, 'N':0}
    choice_dict = {
        1 :	(3, 0),
        2 : (2, 0),
        3 : (1, 0),
        4 : (0, 0),
        5 : (0, 1),
        6 : (0, 2),
        7 : (0, 3)
    }
    
    for i, s in enumerate(survey):
        no, yes = s[0], s[1]
        scores[no] += choice_dict[choices[i]][0]
        scores[yes] += choice_dict[choices[i]][1]
    
    for r in res:
        if scores[r[0]] > scores[r[1]]: 
            answer += r[0]
        elif scores[r[0]] < scores[r[1]]:
            answer += r[1]
        else:
            answer += min(r[0], r[1])
            
    return answer