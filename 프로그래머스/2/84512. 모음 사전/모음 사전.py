dic = {}
visited = {}
index = 1

def dfs(now, target):
    global dic, visited, index
    if len(now) >= 5:
        return
    
    for nxt in ('A', 'E', 'I', 'O', 'U'):
        tmp = now + nxt
        if (tmp not in visited) or not visited[tmp]:
            visited[tmp] = True
            dic[tmp] = index
            index += 1
            dfs(tmp, target)
            visited[tmp] = False


def solution(word):
    global dic, visited, index
    for alp in ('A', 'E', 'I', 'O', 'U'):
        dic[alp] = index
        visited[alp] = True
        index += 1
        dfs(alp, word)
        
    return dic[word]