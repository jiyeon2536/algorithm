def to_days(date):
    # print(date.split('.'))
    return int(date.split('.')[2]) + (int(date.split('.')[1]) * 28) + (int(date.split('.')[0]) * 12 * 28)
    

def solution(today, terms, privacies):
    answer = []
    
    term_dict = {}
    for term in terms:
        term_dict[term.split(' ')[0]] = int(term.split(' ')[1]) * 28

    for i, p in enumerate(privacies):
        date, t = p.split(' ')
        if to_days(today) >= (to_days(date) + term_dict[t]):
            answer.append(i + 1)
        
    return answer