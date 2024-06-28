def solution(participant, completion):
    name = {}
    for p in participant:
        if p in name:
            name[p] += 1
        else:
            name[p] = 1
            
    for c in completion:
        name[c] -= 1
    
    for b in name:
        if name[b] > 0:
            return b