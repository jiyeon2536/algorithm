def solution(num_list):
    diff = num_list[-1] - num_list[-2]
    if diff > 0:
        return num_list + [diff]
    return num_list + [num_list[-1] * 2]
    
