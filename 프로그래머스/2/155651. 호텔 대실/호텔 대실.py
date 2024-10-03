def time_in_min(time, is_end):
    [h, m] = time.split(':')
    converted = int(h) * 60 + int(m)
    return converted + 10 if is_end else converted


def solution(book_time):
    answer = 0
    std_book_time = sorted(book_time)
    rooms = [] # 스택
    
    for st, end in std_book_time:
        st_in_min = time_in_min(st, False)
        after_clean = time_in_min(end, True)
        # 초깃값
        if not rooms:
            answer += 1
            rooms.append(after_clean)
        else:
            if rooms[-1] > st_in_min :
                answer += 1 # 방을 하나 더 만듦
            else:
                rooms.pop() # 이미 나간 사람이니까 빼줌
            rooms.append(after_clean)
            
        rooms.sort(reverse=True)
    
    return answer






