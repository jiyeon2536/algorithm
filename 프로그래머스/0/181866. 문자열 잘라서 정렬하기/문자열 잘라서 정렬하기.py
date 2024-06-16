def solution(myString):
    a = myString.split('x')
    return sorted([i for i in a if i])