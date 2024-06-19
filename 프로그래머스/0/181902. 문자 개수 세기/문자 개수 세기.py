def solution(my_string):
    result = [0 for _ in range(52)]
    for m in my_string:
        if m.isupper():
            result[ord(m) - ord('A')] += 1
        else:
            result[ord(m) - ord('a') + 26] += 1
    return result