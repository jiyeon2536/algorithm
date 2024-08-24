from collections import Counter
def solution(topping):
    answer = 0
    
    ob = set()
    yb = Counter(topping)
    
    for t in topping:
        yb[t] -= 1
        if yb[t] == 0:
            del yb[t]
        ob.add(t)
        if len(ob) == len(yb):
            answer += 1
    
    return answer