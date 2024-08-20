def make_set(st):
    res = {}
    for i in range(len(st) - 1):
        tmp = st[i:i+2].lower()
        if tmp.isalpha():
            if tmp in res:
                res[tmp] += 1
            else:
                res[tmp] = 1
    return res
    
def solution(str1, str2):
    s1, s2 = make_set(str1), make_set(str2)
    N = 65536
    
    if not (s1 or s2):
        return N
    
    common_el = 0 
    
    for f in s1:
        if f in s2:
            common_el += min(s1[f], s2[f])
            
    return int(common_el / (sum(s1.values()) + sum(s2.values()) - common_el) * N)