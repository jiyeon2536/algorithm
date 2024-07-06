def solution(keymap, targets):
    answer = [0] * len(targets)
    
    key_dict = {}
    
    for keys in keymap:
        for i, al in enumerate(keys):
            if al in key_dict:
                key_dict[al] = min(key_dict[al], i + 1)
            else:
                key_dict[al] = i + 1
    
    for idx, target in enumerate(targets):
        accum = 0
        for ch in target:
            if ch not in key_dict:
                answer[idx] = -1
                break
            else:
                accum += key_dict[ch]
        if not answer[idx]:
            answer[idx] = accum
        
    return answer