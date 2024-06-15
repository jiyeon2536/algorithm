def solution(arr1, arr2):
    l1, l2, s1, s2 = len(arr1), len(arr2), sum(arr1), sum(arr2)
    if l1 > l2:
        return 1
    elif l1 < l2:
        return -1
    else:
        if s1 > s2:
            return 1
        elif s1 < s2:
            return -1
        else:
            return 0