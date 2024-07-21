def solution(numbers, hand):
    answer = ''    
    l_fing = 10
    r_fing = 12
    
    # dif = [[1, 3], [2, 4, 6], [5, 7, 9], [8, 10]]
    dif = {0: 0, 1: 1, 2: 2, 3: 1, 4: 2, 5: 3, 6: 2, 7: 3, 8: 4, 9: 3, 10: 4}
    for n in numbers:
        if n in [1, 4, 7]:
            answer += 'L'
            l_fing = n
        elif n in [3, 6, 9]:
            answer += 'R'
            r_fing = n
        else:
            if n == 0:
                n = 11
            l_d = dif[abs(l_fing - n)]
            r_d = dif[abs(r_fing - n)]
            if l_d < r_d:
                answer += 'L'
                l_fing = n
            elif l_d > r_d:
                answer += 'R'
                r_fing = n
            else:
                if hand[0] == 'r':
                    answer += 'R'
                    r_fing = n
                else:
                    answer += 'L'
                    l_fing = n
            
    return answer