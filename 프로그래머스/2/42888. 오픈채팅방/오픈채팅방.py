def solution(record):
    answer = []
    id_nick = {}
    # 먼저 uid랑 닉네임 매핑해줌
    for r in record:
        [msg, *user] = r.split(' ')
        if len(user) > 1:
            id_nick[user[0]] = user[1]
            
    for r in record:
        [msg, *user] = r.split(' ')
        nickname = user[0]
        if msg[0] == 'E':
            answer.append(f'{id_nick[nickname]}님이 들어왔습니다.')
        if msg[0] == 'L':
            answer.append(f'{id_nick[nickname]}님이 나갔습니다.')
    
    return answer