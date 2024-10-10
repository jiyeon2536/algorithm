from itertools import permutations

def is_matched(uid, bid):
    u_len = len(uid)
    if u_len != len(bid):
        return False
    for i in range(u_len):
        if bid[i] != '*' and (uid[i] != bid[i]):
            return False
    return True


# 중복
def is_duplicated(perm, candi):
    if sorted(perm) in candi:
        return True
    return False

    
def solution(user_id, banned_id):
    candi = []
    answer = 0
    b_len = len(banned_id)
    perm_arr = list(permutations(user_id, b_len))
    
    for perm in perm_arr:
        flag = True
        for i in range(b_len):
            if is_matched(perm[i], banned_id[i]) == False:
                flag = False
                break
        # 다 돌았는데 살아남았으면, 중복값이 없으면 
        if flag and (not is_duplicated(perm, candi)):
            answer += 1
            candi.append(sorted(perm))
            
    return answer