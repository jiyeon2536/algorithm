def solution(sizes):
    max_big, max_small = 0, 0
    for size in sizes:
        bigger = max(size[0], size[1])
        smaller = min(size[0], size[1])
        max_big = max(bigger, max_big)
        max_small = max(smaller, max_small)
    return max_big * max_small