def solution(absolutes, signs):
    return sum([absolutes[i] if signs[i] else -1 * absolutes[i] for i in range(len(absolutes))])