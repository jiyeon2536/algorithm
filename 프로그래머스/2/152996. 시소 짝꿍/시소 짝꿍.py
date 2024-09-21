from collections import Counter

def solution(weights):
    answer = 0
    dic = Counter(weights)
    print(dic)
    weights.sort()
    
    for weight in weights:
        answer += dic[weight] - 1  # 나를 제외한 짝꿍 수
        dic[weight] -= 1  # 나를 빼줌
        answer += dic[weight * 2]  # 나랑 4 2 거리에 있는 짝꿍
        if (weight * 3) % 2 == 0:
            answer += dic[weight * 3 // 2] # 나랑 3 2 거리에 있는 짝꿍
        if (weight * 4) % 3 == 0:
            answer += dic[weight * 4 // 3] # 나랑 4 3 거리에 있는 짝꿍
        
    return answer