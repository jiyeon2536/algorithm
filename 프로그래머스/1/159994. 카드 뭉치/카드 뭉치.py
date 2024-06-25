def solution(cards1, cards2, goal):
    c1 = ''
    c2 = ''
    for g in goal:
        if g in cards1:
            c1 += g
        elif g in cards2:
            c2 += g
    return "Yes" if (c1 in ''.join(cards1) and c2 in ''.join(cards2)) else "No"