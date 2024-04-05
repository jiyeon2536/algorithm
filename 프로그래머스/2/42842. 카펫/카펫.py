def solution(brown, yellow):
    answer = []
    
    s = brown + yellow
    
    for w in range(3, s // 3 + 1):
        h = s // w
        if (w * h == s) :
            if (brown == (2 * (w + h - 2))):
                if (yellow == ((w - 2) * (h - 2))):
                    answer = [w, h]
    return answer