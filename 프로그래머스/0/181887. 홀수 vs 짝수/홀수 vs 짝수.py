def solution(num_list):
    s1 = 0
    s2 = 0
    for i, n in enumerate(num_list):
        if i % 2:
            s1 += n
        else:
            s2 += n
    return max(s1, s2)