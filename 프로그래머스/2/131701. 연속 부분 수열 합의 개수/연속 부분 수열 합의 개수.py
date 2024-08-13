def solution(elements):
    length = len(elements)
    sum_set = set()
    # 수열의 길이
    for i in range(1, length + 1):
        # 시작 지점
        for j in range(length):
            if (j+i) <= length:
                sum_set.add(sum(elements[j:(j+i)]))
            else:
                sum_set.add(sum(elements[j:length]) + sum(elements[:j+i-length]))

    return len(sum_set)