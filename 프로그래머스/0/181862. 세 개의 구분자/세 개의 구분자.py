def solution(myStr):
    return [i for i in myStr.replace('a', 'c').replace('b', 'c').split('c') if i] or ['EMPTY']