def solution(skill, skill_trees):
    answer = 0
    for sk in skill_trees:
        q = list(skill)
        flag = True
        for s in sk:
            if s in skill and q.pop(0) != s:
                flag = False
                break
        if flag : answer += 1
                
    return answer