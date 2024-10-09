def solution(genres, plays):
    answer = []
    result = []
    p_dict = {}
    g_dict = {}
    
    for i, genre in enumerate(genres):
        if genre not in p_dict:
            p_dict[genre] = 0
            g_dict[genre] = []
        p_dict[genre] += plays[i]
        g_dict[genre].append([i, plays[i]])

    for k, v in g_dict.items():
        v.sort(key= lambda x:x[1], reverse=True)
        answer.append([v[:2], p_dict[k]])
        
    answer.sort(key=lambda x:x[-1], reverse=True)
    
    for [data , _] in answer:
        for [idx, play] in data:
            result.append(idx)

    return result