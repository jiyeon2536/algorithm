# 1단계
def to_lower(new_id):
    lower = ''
    for i in new_id:
        if i.isupper():
            lower += i.lower()
        else:
            lower += i
    return lower

# 2단계
def no_symbol(new_id):
    no_sym = ''
    for i in new_id:
        if ('a' <= i <= 'z') or i.isdigit() or (i in ['-', '_', '.']):
            no_sym += i
    return no_sym

# 3단계
def one_dot(new_id):
    while '..' in new_id:
        new_id = new_id.replace('..', '.')
    return new_id

# 4단계
def middle(new_id):
    mid = new_id
    if new_id[0] == '.':
        mid = mid[1:]
    if new_id[-1] == '.':
        mid = mid[:-1]
    return mid

# 5단계
def no_empty(new_id):
    return new_id if len(new_id) > 0 else 'a'

# 6단계
def shorter(new_id):
    if len(new_id) <= 15:
        return new_id
    elif new_id[14] == '.':
        return new_id[:14]
    else:
        return new_id[:15]

# 7단계
def longer(new_id): 
    if len(new_id) == 2: 
        return new_id + new_id[-1]
    elif len(new_id) == 1:
        return new_id * 3
    else:
        return new_id
        
def solution(new_id):    
    return longer(shorter(no_empty(middle(one_dot(no_symbol(to_lower(new_id)))))))